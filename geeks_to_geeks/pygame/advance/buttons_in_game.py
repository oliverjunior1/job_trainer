import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((720,720))

# text
font = pygame.font.SysFont('Times New Roman',25)
text = font.render('quit', True, 'white')
text_rect = text.get_rect()
text_rect.center=(360,360)

# draw
draw = pygame.draw.rect(screen, 'red', (315,340,100,35))

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
    pygame.display.flip()