#-------------------Pygame--------------------------------------------
# import pygame
# import sys
#
# pygame.font.init()
# pygame.font.get_fonts()
#
# screen = pygame.display.set_mode((500,500))
#
# draw = pygame.draw.rect(screen, (255,0,0), (30,30,20,20))
#
# font = pygame.font.SysFont('Times New Roman', 50)
# text = font.render('Jesus is the love', True, (40,40,30,30))
# text_rect = text.get_rect()
# text_rect.center=(250,250)
#
# while True:
#     screen.blit(text, text_rect)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#             pygame.quit()
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_1:
#                 screen.fill((0,0,255))
#             elif event.key==pygame.K_2:
#                 screen.fill((0,150,120))
#     pygame.display.flip()
#
#---------------------------------Pandas--------------------------
import pandas as pd
import numpy as np

ser = pd.Series()
