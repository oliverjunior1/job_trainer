import pygame

pygame.init()

display = pygame.display.set_mode((400,400))
image = pygame.image.load('../beginning/plant.png')
display.blit(image,(100,100))
pygame.time.wait(5000)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

pygame.quit()