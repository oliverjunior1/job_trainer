import pygame
import sys

pygame.init()
display = pygame.display.set_mode((600,600))
display.fill((255,255,255))
pygame.draw.line(display,(0,0,0),[100,300],[500,300],5)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()