import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((400,400))
color = (48,141,70)
rect = pygame.Rect(30,30,60,60)
pygame.draw.rect(surface, color, rect,2,5)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()