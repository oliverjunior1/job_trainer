import pygame
import sys

pygame.init()
display = pygame.display.set_mode((500,500))
image = pygame.image.load('gfg-gg-logo.svg')
display.blit(image,(100,100))
pygame.time.wait(5)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()

    pygame.display.flip()