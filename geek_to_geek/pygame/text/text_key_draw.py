import pygame
import sys

pygame.font.init()
pygame.font.get_fonts()

screen = pygame.display.set_mode((500,500))
pygame.draw.rect(screen, (255,255,255),(70,280,350,30))

font = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('Lucida Console', 14)
text = font.render('Jesus is the way,', True, (255,255,255))
text2 = font2.render('type left and right on the keyboard to see all the message!', True, (100,150,100))
text_rect2 = text2.get_rect()
text_rect2.center=(250,200)
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                text = font.render('and the life!', True, (100, 100, 100))
                text_rect.bottom=(350)
            if event.key==pygame.K_RIGHT:
                text = font.render('the truth,', True, (255, 0, 0))
                text_rect.center=(250,300)
    pygame.display.flip()