import pygame

pygame.init()

screen = pygame.display.set_mode((400,300), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
