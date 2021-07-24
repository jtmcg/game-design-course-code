# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:04:16 2019

@author: J. Tyler McGoffin
"""

import pygame, sys, dungeontile
from monster import Monster
from pygame.locals import *

class Map:
    
    def __init__(self):
        self.map = []
        self.currentTile = 0
        self.setUp()
        
    def setUp(self):
        #create a random order of dungeon tiles and fill them with random stuff
        dungeonStart = dungeontile.DungeonTile(None, None, "start", False)
        dungeon2 = dungeontile.DungeonTile(None, Monster(speed = 4), "center", False)
        dungeon3 = dungeontile.DungeonTile(None, Monster(speed = 8), "center", False)
        dungeon5 = dungeontile.DungeonTile(None, None, "end", False)
        
        self.map = [dungeonStart, dungeon2, dungeon3, dungeon5]
                
    def transitionTile(self, direction):
        if direction == 'right':
            if self.map[self.currentTile].type == "end":
                return True
            else:
                self.currentTile += 1
        elif direction == 'left' and self.currentTile != 0:
            self.currentTile -= 1
        return False
            
    def drawCurrentTile(self):
        return self.map[self.currentTile].image