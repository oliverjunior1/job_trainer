#---------------------------lambda---------------------------------------
# x = lambda a, b: a **b
#
# print(x(5,3))
#---------------------------list_comprehension---------------------------
# list = [1,2,3,4,5,6,7,8,9,10]
#
# list_2 = [x**3 for x in list]
#
# print(list_2)
#-----------------------------try_except----------------------------------
# try:
#     x = 20/0
#     print(x)
# except:
#     print('Not divisible for zero!')
#-----------------------------mega---------------------------------------
# import random
# def lucky():
#     x = random.sample(range(1,61),6)
#     return sorted(x)
# y = lucky()
# print(y)
#---------------------------pygame---------------------------------------
import pygame
import sys

from narwhals import scan_csv

pygame.init()
drawer = (40,40,30,30)
screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'red', drawer)

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the World!', True, 'blue')
text_rect = text.get_rect()
text_rect.center=(250,250)
# ending
while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                draw = pygame.draw.rect(screen, 'green', drawer)
            elif event.key==pygame.K_DOWN:
                draw = pygame.draw.rect(screen, 'pink', drawer)
    pygame.display.flip()
