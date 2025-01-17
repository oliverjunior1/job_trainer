import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
Icon = pygame.image.load('plant.png')
pygame.display.set_icon(Icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()