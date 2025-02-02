import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
image = pygame.image.load('gfg-gg-logo.svg')
screen.blit(image,(100,100))
pygame.time.wait(5000)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
pygame.display.flip()
pygame.quit()