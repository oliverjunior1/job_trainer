#Type the letter for show the color in the screen
import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((300,300))
# Screen colors disponible
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_w:
                surface.fill(WHITE)
            elif event.key ==pygame.K_b:
                surface.fill(BLUE)
            elif event.key ==pygame.K_l:
                surface.fill(BLACK)
            elif event.key ==pygame.K_r:
                surface.fill(RED)
            elif event.key ==pygame.K_g:
                surface.fill(GREEN)
    pygame.display.flip()


