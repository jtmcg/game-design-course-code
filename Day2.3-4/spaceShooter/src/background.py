# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:59:14 2019

@author: Stanford
"""

import pygame

class Background:
    
    def __init__(self, bgType, WINDOWHEIGHT):
        if bgType == "background":
            self.image = pygame.image.load("ArtAssets7/spacebackground.png")
            self.scrollSpeed = 1
        elif bgType == "paralax":
            self.image = pygame.image.load("ArtAssets7/spaceparalax.png")
            self.scrollSpeed = 2
            
        self.WINDOWHEIGHT = WINDOWHEIGHT 
        
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOWHEIGHT
        
    def move(self):
        self.rect.bottom += self.scrollSpeed
        if self.rect.top == 0:
            self.rect.bottom = self.WINDOWHEIGHT