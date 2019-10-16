# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:17:47 2019

@author: Stanford
"""

import pygame

class Ship:
    
    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT): #These are not global variables here but arguments passed to this class.
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets7/ship.png"), (80,80)) #Resize as loaded
        self.rect = self.image.get_rect()
        
        self.leftLimit = 10
        self.rightLimit = WINDOWWIDTH - 10
        self.topLimit = 10
        self.bottomLimit = WINDOWHEIGHT - 10
        
        self.moveSpeed = 5 #pixels per frame
        
        self.setStartPos()
        
    def move(self, left, right, up, down):
        if left and self.rect.left >= self.leftLimit:
            self.rect.left -= self.moveSpeed
        if right and self.rect.right <= self.rightLimit:
            self.rect.left += self.moveSpeed
        if up and self.rect.top >= self.topLimit:
            self.rect.top -= self.moveSpeed
        if down and self.rect.bottom <= self.bottomLimit:
            self.rect.top += self.moveSpeed
        
    def setStartPos(self):
        #spawns ship in start position. Using Center Point for control
        xCoord = (self.rightLimit + self.leftLimit) / 2
        yCoord = self.bottomLimit - self.rect.height/2
        
        self.rect.center = (xCoord, yCoord)