import pygame
import sys

pygame.init()
surface = pygame.display.set_mode((800,300))
color = (255,0,0)
rect = (30,30,40,40)
pygame.draw.rect(surface,color,rect)
pygame.display.set_caption('Event Handling')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                print('Mouse moving to the right')
            elif event.rel[1] > 0:
                print('Mouse moving down')
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print('Right mouse button pressed')
        elif event.type == pygame.MOUSEBUTTONUP:
            print('Mouse button has been released')
    pygame.display.flip()