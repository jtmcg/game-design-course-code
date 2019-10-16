# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:04:09 2019

@author: Stanford
"""

import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame Intro")

#Color      = (  R,   G,   B)
BLACK       = (  0,   0,   0)
WHITE       = (255, 255, 255)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
BLUE        = (  0,   0, 255)
PURPLE      = (128,   0, 128)
BGCOLOR     = WHITE

# draw some shapes on the screen
DISPLAYSURF.fill(BGCOLOR)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0),(291,106),(236,277),(56, 277),(0,106))) #(surface, color, vertices)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4) #(surface, color, start point, end point, thickness)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, PURPLE, (300, 50), 20, 4) #(surface, color, center, radius, thickness)
pygame.draw.ellipse(DISPLAYSURF, RED, (40, 80,250,200), 1) #(surface, color, (rect))
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50)) #(surface, color, (rect))


while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()