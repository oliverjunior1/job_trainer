import pygame
import sys

pygame.font.init()
# Put the fonts from the system usable
pygame.font.get_fonts()

# About the size of screen
screen = pygame.display.set_mode((500,500))
# To draw a rectangle
pygame.draw.rect(screen, (255,255,255),(70,280,350,30))

# About text
font = pygame.font.SysFont('freesanbold.ttf', 50)# specific fonts will be better
font2 = pygame.font.SysFont('Lucida Console', 14)# If I put system fonts won't show, if it isn't installed
text = font.render('Jesus is the way,', True, (255,255,255))
text2 = font2.render('type left and right on the keyboard to see all the message!',
                     True, (100,150,100))
text_rect2 = text2.get_rect()
text_rect2.center=(250,200)
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    # About the position of the text
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)
    # to make possible finish the program
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        # The options to use the keyboard
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                text = font.render('and the life!', True, (100, 100, 100))
                text_rect.bottom=(350)
            if event.key==pygame.K_RIGHT:
                text = font.render('the truth,', True, (255, 0, 0))
                text_rect.center=(250,300)
                # About the frames
    pygame.display.flip()