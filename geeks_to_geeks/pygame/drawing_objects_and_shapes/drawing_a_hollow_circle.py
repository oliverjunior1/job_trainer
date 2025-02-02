import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600,600))

window.fill((255,255,255))

pygame.draw.circle(window,(0,255,0),[300,300],170,3)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

pygame.display.update()