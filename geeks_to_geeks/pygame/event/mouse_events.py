import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((400,400))
surface.fill((255,255,255))
color= (0,0,255)
rect = pygame.Rect(30,30,40,40)
pygame.draw.rect(surface,color,rect,7,0,0,0,0,0)

while True:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                print('Mouse moving to the right')
            elif event.rel[1]>0:
                print('Mouse moving down')
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print('Right mouse button pressed')
        elif event.type==pygame.MOUSEBUTTONUP:
            print('Mouse button has been released')
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()