import pygame
import sys

pygame.init()
pygame.font.init()
pygame.font.get_init()
display_surface = pygame.display.set_mode((500,500))
pygame.display.set_caption('About Jesus')
font = pygame.font.SysFont('freesanbold.ttf',50)
txt = font.render('Jesus is the light of the World!', True, (0,0,0))
text_rect = txt.get_rect()
text_rect.center=(250,250)

while True:
    display_surface.blit(txt, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_b:
                display_surface.fill((0,0,255))
            elif event.key==pygame.K_w:
                display_surface.fill((255,255,255))
            elif event.key==pygame.K_g:
                display_surface.fill((0,255,0))
            elif event.key==pygame.K_r:
                display_surface.fill((255,0,0))
    pygame.display.flip()