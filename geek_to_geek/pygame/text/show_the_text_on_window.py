import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))

font = pygame.font.SysFont('freesanbold.ttf', 50)
text = font.render('Jesus is the light of the world!',True, (0,0,0))
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.fill((255,255,255))
    screen.blit(text,text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()


