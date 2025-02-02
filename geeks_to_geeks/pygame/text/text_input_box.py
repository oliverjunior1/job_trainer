import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600,500])
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200,200,140,32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()