import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
# draw
pygame.draw.rect(screen, (0,0,0), (40,40,30,30))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the World!', True, (0,255,0))
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                pygame.draw.rect(screen, (0, 0, 0), (50, 50, 50, 50))
            if event.key==pygame.K_2:
                pygame.draw.rect(screen, (0, 0, 0), (100,100,100,100))
            if event.key==pygame.K_3:
                pygame.draw.rect(screen, (0, 0, 0), (120, 120, 120, 120))
    pygame.display.flip()