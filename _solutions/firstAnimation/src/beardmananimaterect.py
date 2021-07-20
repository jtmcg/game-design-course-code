import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

WHITE = (255, 255, 255)
beardManImg = pygame.image.load("../ArtAssets5/beardManSmall.png") # load image based on relative location
beardManRect = beardManImg.get_rect()
direction = "right"
SPEED = 5 # pixels per frame

beardManImgRight = beardManImg
beardManImgLeft = pygame.transform.flip(beardManImg, True, False)
currentBeardMan = beardManImgRight

while True:
    DISPLAYSURF.fill(WHITE)

    # Fill in drawing and animating here
    if direction == "right":
        beardManRect.left += 5
        if beardManRect.right >= 790:
            direction = "down"
    elif direction == "down":
        beardManRect.top += 5
        if beardManRect.bottom >= 590:
            direction = "left"
            currentBeardMan = beardManImgLeft
    elif direction == "left":
        beardManRect.left -= 5
        if beardManRect.left <= 10:
            direction = "up"
    elif direction == "up":
        beardManRect.top -= 5
        if beardManRect.top <= 10:
            direction = "right"
            currentBeardMan = beardManImgRight

    DISPLAYSURF.blit(currentBeardMan, beardManRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)