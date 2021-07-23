# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:23:42 2019

@author: J. Tyler McGoffin
"""

import pygame
from pygame.locals import *

class DungeonTile:
    
    def __init__(self, loot, monster, tileType, locked):
        self.loot = loot
        self.monster = monster
        self.type = tileType
        self.locked = locked
        
        if self.type == "start":
            self.image = pygame.image.load("ArtAssets9/dungeonStartTile.png")
        elif self.type == "center":
            self.image = pygame.image.load("ArtAssets9/dungeonCentralTile.png")
        elif self.type == "end":
            self.image = pygame.image.load("ArtAssets9/exitTile.png")
        