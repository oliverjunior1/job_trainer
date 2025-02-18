import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Moving rectangle')

y = 200
x = 200

width = 10
height = 10

vel = 10

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))

    pygame.display.update()

pygame.quit()