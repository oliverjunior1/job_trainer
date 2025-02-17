import pygame
import sys


pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((720,720))
width = screen.get_width()
height = screen.get_height()
# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('quit', True, 'white')
text_rect = text.get_rect()
text_rect.center=(360,360)

# design button
rect = pygame.draw.rect(screen, 'red', (320,340,80,40))

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if width/2 or height/2:
                pygame.quit()


    pygame.display.flip()