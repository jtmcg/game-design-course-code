# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:15:15 2019

@author: J. Tyler McGoffin

Source: "Making Games with Python & Pygame" by Al Sweigart. Chapter 2.
"""

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("BEARD MAN!!")

WHITE = (255, 255, 255)
beardManImg = pygame.image.load("ArtAssets5/beardman.png")
beardManRect = beardManImg.get_rect()
direction = "right"

while(True):
    DISPLAYSURF.fill(WHITE)
    
    if direction == "right":
        beardManRect.left += 5
        if beardManRect.right >= 790: #page 20 has rect attributes
            direction = "down"
    elif direction == "down":
        beardManRect.top += 5
        if beardManRect.bottom >= 590:
            direction = "left"
    elif direction == "left":
        beardManRect.left -= 5
        if beardManRect.left <= 10:
            direction = "up"
    elif direction == "up":
        beardManRect.top -= 5
        if beardManRect.top <= 10:
            direction = "right"
            
    DISPLAYSURF.blit(beardManImg, beardManRect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)