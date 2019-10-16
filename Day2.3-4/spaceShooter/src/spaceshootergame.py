# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:26:21 2019

@author: J. Tyler McGoffin
"""

import pygame, sys
import numpy as np
from pygame.locals import *

from ship import Ship
from laser import Laser
from asteroid import Asteroid
from background import Background

#Set up window and frame rate variables
FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 700

#Set up some Color variables
BLACK = (0, 0, 0)
NAVYBLUE = (0, 0, 128)
DARKPURPLE = (100, 0, 100)
WHITE = (255, 255, 255)
DARKGRAY = (100, 100, 100)

#Start the game
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT #True globals
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Space Shooter")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    
    showStartScreen()
    while(True):
        runGame()
        showGameOverScreen()
        
def runGame():
    #set up the game
    score = 0
    lives = 3
    levelUp = False
    
    #Create our Game Objects: ship, asteroids, lasers
    playerShip = Ship(WINDOWWIDTH, WINDOWHEIGHT)
    leftHeld = False
    rightHeld = False
    upHeld = False
    downHeld = False
    firing = False
    
    #Laser Stuff
    lasers = initializeObjects(10) #reusable code to create an empty object list
    fireRate = 4 #lasers per second
    laserIndex = 0
    laserSpeed = 10
    
    #Asteroid stuff
    asteroids = initializeObjects(25)
    spawnRate = 1 #on average, we'll spawn 1 asteroid per second. We can change this with the code later
    minAsteroidSpeed = 1 #Pixels per frame. We'll change these with the code later
    maxAsteroidSpeed = 6 #Pixels per frame. We'll change these with the code later
    asteroidIndex = 0
    
    #Background stuff
    backgroundObject = Background("background", WINDOWHEIGHT)
    paralaxObject = Background("paralax", WINDOWHEIGHT)
    
    #Main game Loop
    while(True):
        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                #Check for keys down to toggle variables
                elif event.key == K_a or event.key == K_LEFT:
                    leftHeld = True
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = True
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = True
                elif event.key == K_w or event.key == K_UP:
                    upHeld = True
                elif event.key == K_SPACE:
                    firing = True
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    leftHeld = False
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = False
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = False
                elif event.key == K_w or event.key == K_UP:
                    upHeld = False
                elif event.key == K_SPACE:
                    firing = False
        
        #Increase the difficulty of our game
        if score % 10 == 0 and levelUp:
            minAsteroidSpeed += 2
            maxAsteroidSpeed += 2
            spawnRate += 1
            levelUp = False
        elif score % 10 != 0:
            levelUp = True
        
        #Laser Firing
        if firing:
            lasers[laserIndex] = Laser(playerShip.rect, laserSpeed)
            firing = False
            laserIndex += 1
            if laserIndex >= len(lasers):
                laserIndex = 0
                
        #automate asteroid spawning
        if np.random.randint(0, FPS/spawnRate) == 0:
            asteroids[asteroidIndex] = Asteroid(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minAsteroidSpeed, maxAsteroidSpeed))
            asteroidIndex += 1
            if asteroidIndex >= len(asteroids):
                asteroidIndex = 0
                
        #Move Stuff
        for laser in lasers:
            if laser != None:
                laser.move()
        for asteroid in asteroids:
            if asteroid != None:
                asteroid.move()
        playerShip.move(leftHeld, rightHeld, upHeld, downHeld)
        backgroundObject.move()
        paralaxObject.move()
        
        #Collision Handling
        for currentAsteroidIndex, asteroid in enumerate(asteroids): #use enumerator so we can modify asteroids list while looping through it
            if asteroid != None: #None type can't collide
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(asteroid.rect):
                            asteroids[currentAsteroidIndex] = None
                            lasers[currentLaserIndex] = None
                            score += 1
                #check for a collision with the player
                if playerShip.rect.colliderect(asteroid.rect):
                    lives -= 1
                    if lives > 0:
                        playerHit() #here we'll write our reset code
                        playerShip.setStartPos() #reset our player's start pos
                        asteroids = initializeObjects(25) #reset our asteroids
                        lasers = initializeObjects(10) #reset our lasers
                    else:
                        return #Game over. Leave the runGame() function
                    break #exit the loop after detecting a player collision
        
        #Draw a bg to work with
        DISPLAYSURF.fill(BLACK)
        #Draw our components on the screen
        draw(backgroundObject.image, backgroundObject.rect) #Order matters here!!!!
        draw(paralaxObject.image, paralaxObject.rect)
        draw(playerShip.image, playerShip.rect) #args = imageSurf, imageRect
        drawLasers(lasers)
        drawAsteroids(asteroids)
        drawHUD(lives, score) #Should be drawn above everything else
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawHUD(lives, score):
    healthBarSurf = BASICFONT.render("Ships remaining: "+str(lives), True, WHITE)
    healthBarRect = healthBarSurf.get_rect()
    healthBarRect.topright = (WINDOWWIDTH - 10, 10)
    draw(healthBarSurf, healthBarRect)
    
    scoreSurf = BASICFONT.render("Asteroids destroyed: "+str(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10, 10)
    draw(scoreSurf, scoreRect)

def playerHit():
    hitSurf = BASICFONT.render("You've been destroyed!", True, WHITE)
    hitRect = hitSurf.get_rect()
    hitRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
    draw(hitSurf, hitRect) #Show the hit text

    pygame.display.update()
    pygame.time.wait(2000) #wait 2 seconds before reseting        
        
def initializeObjects(number):
    objects = []
    for x in range(number):
        objects.append(None)
    return objects

def drawAsteroids(asteroids):
    for asteroid in asteroids:
        if asteroid != None:
            image, rect = asteroid.draw() #Slightly different from lasers so we can include the rotation
            draw(image, rect)
        
def drawLasers(lasers):
    for laser in lasers:
        if laser != None:
            draw(laser.image, laser.rect)
        
def draw(image, rect):
    DISPLAYSURF.blit(image,rect)
    
#All of this code was copied from Wormy and modified slightly to our needs        
def terminate():
    pygame.quit()
    sys.exit()
    
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('SPACE', True, WHITE, DARKPURPLE)
    titleSurf2 = titleFont.render('SHOOTER', True, NAVYBLUE)
    
    degrees1 = 0
    degrees2 = 0
    
    while(True): #looks like a game loop
        DISPLAYSURF.fill(BLACK)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7
        
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else:
                return True
    return False
    
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to continue.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2, 10)
    overRect.midtop = (WINDOWWIDTH/2, gameRect.height + 10 + 25)
    
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() #clear the event cache
    
    while(True):
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
    
if __name__ == '__main__':
    main()