import pygame


pygame.init()

window=pygame.display.set_mode((400,400))
color = 'red'

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(color)
    pygame.display.flip()
    if (color == 'red'):
        color = 'green'
    else:
        color = 'red'
pygame.quit()