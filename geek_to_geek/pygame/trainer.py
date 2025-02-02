import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))

# text
font = pygame.font.SysFont('Times New Roman',25)
text = font.render('Jesus is the light of the World!', True, (255,255,255))
text_rect = text.get_rect()
text_rect.center=(250,250)
# draw
pygame.draw.rect(screen, (255,0,0),(100,270,300,50))
while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        # change the screen color
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                screen.fill((255,255,0))
            elif event.key==pygame.K_2:
                screen.fill((0,255,255))
            elif event.key==pygame.K_3:
                screen.fill((255,0,255))
    pygame.display.flip()