import pygame
import sys

pygame.init()
pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))
rect = (0,0,30,30)

font = pygame.font.SysFont('freesanbold.ttf', 50)
text = font.render('Jesus is the way', True, (0,0,255))
text_rect = text.get_rect()
text_rect.center=(250,250)

pygame.draw.rect(screen, (0,0,255), rect)

while True:
    screen.fill((255,255,255))
    screen.blit(text,text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_0:
                text = font.render('Jesus give him life', True, (255,0,0))
            elif event.key == pygame.K_1:
                text = font.render('For us sinner man',True, (200,0,35))
            elif event.key == pygame.K_2:
                text = font.render('Jesus love you!', True, (0, 200, 35))

    pygame.display.flip()
