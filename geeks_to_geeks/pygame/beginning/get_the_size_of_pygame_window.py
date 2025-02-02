import pygame

pygame.init()

screen = pygame.display.set_mode((400,300))

x, y = screen.get_size()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print(x, y)