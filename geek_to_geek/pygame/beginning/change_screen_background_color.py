import pygame

pygame.init()
surface = pygame.display.set_mode((400,400))

color = (255,0,0)

surface.fill(color)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = True


pygame.quit()