import pygame
import sys

from pygame import MOUSEBUTTONDOWN

pygame.init()
display = pygame.display.set_mode((600,600))
display.fill((255,255,255))
circle_positions = []
circle_radius = 60
color = (0,0,255)
run = True

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)
    for position in circle_positions:
        pygame.draw.circle(display,color, position, circle_radius)
    pygame.display.flip()