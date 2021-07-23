# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:46:28 2019

@author: J. Tyler McGoffin
"""

import pygame, sys
from pygame.locals import *

TILELEFT = 50
TILEFLOOR = 500
TILERIGHT = 550
GRAVITY = 1/15
JUMPVELOCITY = 25
RIGHT = 'right'
LEFT = 'left'

class BeardMan:
    
    def __init__(self, speed):
        self.hp = 100
        self.imageRight = pygame.image.load('ArtAssets9/beardManRight.png')
        self.imageLeft = pygame.image.load('ArtAssets9/beardManLeft.png')
        self.image = self.imageRight
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (TILELEFT, TILEFLOOR)
        self.gold = 0
        self.inventory = []
        self.jumping = {"state": False, "duration": 0}
        self.speed = speed

    def move(self, direction, jump):
        if direction != None:
            if direction == RIGHT:
                self.rect.left += self.speed
            if direction == LEFT:
                self.rect.right -= self.speed
        if jump:
            self.jumping["state"] = True
        if self.jumping["state"] == True:
            self.rect.bottom -= int(JUMPVELOCITY + -1*GRAVITY*self.jumping["duration"]**2)
            self.jumping["duration"] += 1
            if self.rect.bottom >= TILEFLOOR:
                self.jumping["state"] = False
                self.rect.bottom = TILEFLOOR
                self.jumping["duration"] = 0
        
        
        
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
        return self.image, self.rect
    
    def flipDirection(self, direction):
        if direction == 'right' and self.image != self.imageRight:
            self.image = self.imageRight
        elif direction == 'left' and self.image != self.imageLeft:
            self.image = self.imageLeft
    