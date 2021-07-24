# Image
# Rect
# move somehow
# detect collisions with the player
import pygame, numpy
from beardmangame import RIGHT, LEFT, FPS
from beardman import TILEFLOOR

class Monster:

    def __init__(self, speed):
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets9/blue_monster.png"), (83,100))
        self.rect = self.image.get_rect()
        self.moveDirection = LEFT
        self.movePauseInterval = 0
        self.paused = True
        self.speed = speed
        self.rect.bottomright = (600, TILEFLOOR)

    def move(self):
        if self.moveDirection == RIGHT and not self.paused:
            self.rect.left += self.speed
        elif self.moveDirection == LEFT and not self.paused:
            self.rect.right -= self.speed
        
        if self.rect.left < 200 and not self.paused:
            self.paused = True
        elif self.rect.right > 600 and not self.paused:
            self.paused = True
        
        if self.paused:
            if self.movePauseInterval == 0:
                self.movePauseInterval = numpy.random.randint(0, FPS)
            else:
                self.movePauseInterval -= 1
        if self.movePauseInterval <= 0 and self.paused:
            self.paused = False
            if self.moveDirection == RIGHT:
                self.moveDirection = LEFT
            else:
                self.moveDirection = RIGHT