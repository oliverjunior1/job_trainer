import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the world!', True, 'white')
text_rect = text.get_rect()
text_rect.center=(250,250)

# draw
draw = pygame.draw.rect(screen, 'red', (30,30,20,20))

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill('lightblue')
            elif event.key==pygame.K_DOWN:
                screen.fill('lightgreen')
            elif event.key == pygame.K_LEFT:
                screen.fill('red')
            elif event.key == pygame.K_RIGHT:
                screen.fill('yellow')
    pygame.display.update()