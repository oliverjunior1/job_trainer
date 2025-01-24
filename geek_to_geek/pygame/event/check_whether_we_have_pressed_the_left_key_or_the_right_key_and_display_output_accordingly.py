import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((800,300))
color = (255,0,0)
rect = (30,30,40,40)
pygame.draw.rect(surface,color, rect)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('You have pressed right arrow key')
            elif event.key == pygame.K_LEFT:
                print('You have pressed left arrow key')
    pygame.display.flip()
quit()