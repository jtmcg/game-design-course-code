# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:35:12 2019

@author: J. Tyler McGoffin
"""

import pygame, sys, beardman, dungeonmap
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TITLESCREEN = pygame.image.load('ArtAssets9/titleImage.png')
WINNERSCREEN = pygame.image.load('ArtAssets9/winner.png')
GAMEOVERSCREEN = pygame.image.load('ArtAssets9/gameOver.png')

#COLORS
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (171,  39,  25)
BLUE        = (  9, 109, 150)
GRAY        = (150, 150, 150)
DARKGRAY    = ( 40,  40,  40)
TEXTRED     = (237,  28,  36)

#Directions
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'
SPACEBAR = 'spacebar'

STEPSIZE = 5

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('The Adventures of Beard Man!')
    
    showInfoScreen('start')
    
    while(True):
        runGame()
        showInfoScreen('gameover')
      
def runGame():
    
    #initialize necessary classes
    gameMap = dungeonmap.Map()
    beardMan = beardman.BeardMan()
    
    winner = False
    held = False
    direction = None
    jump = False
    
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                held = True
                if event.key == K_RIGHT or event.key == K_d:
                    direction = RIGHT
                    beardMan.flipDirection(direction)
                elif event.key == K_LEFT or event.key == K_a:
                    direction = LEFT
                    beardMan.flipDirection(direction)
                elif event.key == K_UP or K_w or K_SPACE:
                    jump = True
                elif event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_k:
                    beardMan.hp = 0
            elif event.type == KEYUP:
                held = False
          
        if direction == RIGHT and held:
            if beardMan.xPosition < 600:
                beardMan.xPosition += STEPSIZE
            else:
                winner = gameMap.transitionTile(direction)
                beardMan.xPosition = beardman.TILELEFT
        elif direction == LEFT and held:
            if beardMan.xPosition > 50:
                beardMan.xPosition -= STEPSIZE
            else:
                winner = gameMap.transitionTile(direction)
                beardMan.xPosition = beardman.TILERIGHT
        
        if winner:
            showInfoScreen('winner')
            winner = reset(beardMan, gameMap)
            held = False
        elif beardMan.hp <= 0:
            showInfoScreen('gameover')
            winner = reset(beardMan, gameMap) 
            held = False
            
        DISPLAYSURF.blit(gameMap.drawCurrentTile(), (0, 0))  
        if gameMap.map[gameMap.currentTile].monster != None:
            DISPLAYSURF.blit(gameMap.map[gameMap.currentTile].drawMonster(), (400, 300))
        if gameMap.map[gameMap.currentTile].loot != None:
            DISPLAYSURF.blit(gameMap.map[gameMap.currentTile].drawLoot(), (400, 300))
        DISPLAYSURF.blit(beardMan.drawBeardMan(), (beardMan.xPosition, beardMan.yPosition))
        drawHUD()

        pygame.display.update()
        FPSCLOCK.tick(FPS)          
            
def terminate():
    pygame.quit()
    sys.exit()
    
def drawHUD():
    None
        
def showInfoScreen(theType):
    
    if theType == 'start':
        screen = TITLESCREEN
    elif theType == 'winner':
        screen = WINNERSCREEN
    elif theType == 'gameover':
        screen = GAMEOVERSCREEN
        
    while(True):
        DISPLAYSURF.blit(screen, (0,0))
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get()
            return
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def reset(beardMan, gameMap):
    beardMan.xPosition = beardman.TILELEFT
    beardMan.hp = 100
    gameMap.currentTile = 0
    return False
        
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play!', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    
    keyDownEvents = pygame.event.get(KEYDOWN)
    if len(keyDownEvents) == 0:
        return None
    if keyDownEvents[0].key == K_ESCAPE:
        terminate()
    return keyDownEvents[0].key

if __name__ == '__main__':
    main()