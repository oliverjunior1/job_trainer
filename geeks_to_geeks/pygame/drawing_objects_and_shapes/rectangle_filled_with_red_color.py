import pygame
import sys

pygame.init()
display = pygame.display.set_mode((400,300))
color = (255,0,0)
pygame.draw.rect(display,color, pygame.Rect(30,30,60,60))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

