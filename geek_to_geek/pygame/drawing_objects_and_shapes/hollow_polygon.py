import pygame
import sys

pygame.init()

display = pygame.display.set_mode((600,600))
display.fill((255,255,255))
pygame.draw.polygon(display,(255,0,0),[[300,300],[100,400],[100,300]],5)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()