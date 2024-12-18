import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500),0,32)
sprite1 = pygame.image.load('../../pythonProject/images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50,50))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
pygame.display.set_caption("Hello Sprite")
screen.fill((0,0,0))

game_over = False
x, y = (0,0)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5
    if pressed[K_DOWN]:
        y+= 0.5
    if pressed[K_LEFT]:
        x -= 0.5
    if pressed[K_RIGHT]:
        x += 0.5
    screen.blit(sprite1, (x, y) )
    pygame.display.update()
pygame.quit()