import pygame
import sys

pygame.init()
surface = pygame.display.set_mode((300,300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            print('A key has been pressed')
    pygame.display.flip()
