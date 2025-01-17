import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('GeekForGeek')

running = True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False

pygame.quit()