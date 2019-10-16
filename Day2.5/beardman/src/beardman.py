# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:46:28 2019

@author: jtmcgoffin
"""

import pygame, sys
from pygame.locals import *

TILELEFT = 53
TILEFLOOR = 330
TILERIGHT = 550

class BeardMan:
    
    def __init__(self):
        self.hp = 100
        self.imageRight = pygame.image.load('ArtAssets9/beardManRight.png')
        self.imageLeft = pygame.image.load('ArtAssets9/beardManLeft.png')
        self.image = self.imageRight
        self.xPosition = TILELEFT
        self.yPosition = TILEFLOOR
        self.gold = 0
        self.inventory = []
        
    def modifyHealth(self, value):
        self.hp += value
    
    def lootItem(self, item):
        if isinstance(item, int):
            self.gold += item
        elif item not in self.inventory:
            self.inventory.append(item)
        else:
            return "You can't carry any more of those" 
        
    def loseItem(self, item):
        if isinstance(item, int):
            self.gold -= item
        else:
            self.inventory.remove(item)
            
    def drawBeardMan(self):
        return self.image
    
    def flipDirection(self, direction):
        if direction == 'right' and self.image != self.imageRight:
            self.image = self.imageRight
        elif direction == 'left' and self.image != self.imageLeft:
            self.image = self.imageLeft
    