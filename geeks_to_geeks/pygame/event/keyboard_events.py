import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((400,400))

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                print('Move the character forward')
            elif event.key==pygame.K_s:
                print('Move the characher backwards')
            elif event.key==pygame.K_a:
                print('Move the character left')
            elif event.key==pygame.K_d:
                print('Move the character right')
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()