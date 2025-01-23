import pygame
import sys

pygame.init()
display = pygame.display.set_mode((400,400))
color = (255,0,0)
pygame.draw.rect(display,color, pygame.Rect(30,30,60,60),2)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()