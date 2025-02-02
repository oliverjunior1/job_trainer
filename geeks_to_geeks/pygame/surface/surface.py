# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((400,400))
# icon = pygame.image.load('../beginning/plant.png')
# pygame.display.set_icon(icon)
# color = 'red'
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.draw.rect(screen, color, pygame.Rect(30,30,60,60))
#
# pygame.display.flip()
#
# pygame.quit()

# import pygame
#
# pygame.init()
#
# sample_surface = pygame.display.set_mode((400,400))
#
# color = (255,255,0)
# sample_surface.fill(color)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# pygame.display.flip()
# pygame.quit()

import pygame

pygame.init()

display_surface = pygame.display.set_mode((400,400))
image = pygame.image.load('../beginning/plant.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
display_surface.blit(image(100,100))
pygame.quit()