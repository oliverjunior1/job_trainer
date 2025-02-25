import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()
screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'pink', (40,40,30,30))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the World!', True, 'blue')
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill('white')
            elif event.key==pygame.K_DOWN:
                screen.fill('lightblue')
            elif event.key==pygame.K_SPACE:
                screen.fill('lightgreen')
    pygame.display.flip()