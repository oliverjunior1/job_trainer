import pygame
import sys

pygame.init()

display = pygame.display.set_mode((600,600))
display.fill((255,255,255))
pygame.draw.rect(display,(0,0,255),[50,200,500,200])
pygame.draw.circle(display,(0,255,0),[300,300],100)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()
