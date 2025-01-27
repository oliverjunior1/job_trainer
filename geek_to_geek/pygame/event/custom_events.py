import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((800,500))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
rect = (40,40,500,300)
pygame.draw.rect(surface, GREEN, rect)
timer = pygame.time.Clock()
pygame.display.set_caption('Custom Events')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()