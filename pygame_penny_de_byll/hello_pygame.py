import pygame
from pygame.examples.go_over_there import screen

pygame.init()
screen = pygame.display.set_mode((640,840),0,32)
pygame.display.set_caption("Hello Pygame")
screen.fill((0,0,0))