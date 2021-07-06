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
    
if __name__ == '__main__':
    main()