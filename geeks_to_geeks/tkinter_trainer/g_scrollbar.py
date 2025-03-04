import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, (255,0,0), (40,40,30,30))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the world!', True, (0,255,255))
text_rect = text.get_rect()
text_rect.center=(250,250)
# finish
while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                screen.fill((0,0,0))
                text2 = font.render('Jesus is at door and knock...', True, (0,255,0))
                text_rect.center=(250,250)
                screen.blit(text2, text_rect)
            elif event.key==pygame.K_2:
                screen.fill((0,0,0))
                text3 = font.render('The Lord is my shepherd, I will lack nothing', True, (0,0,255))
                text_rect.center=(250,250)
                screen.blit(text3, text_rect)
    pygame.display.flip()