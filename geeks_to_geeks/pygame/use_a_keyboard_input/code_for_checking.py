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
            if event.key==pygame.K_a:
                print('key a is typed')
            elif event.key==pygame.K_j:
                print('key j is typed')
            elif event.key==pygame.K_p:
                print('key p is typed')
            elif event.key==pygame.K_m:
                print('key m is typed')
    pygame.display.flip()
