import pygame

pygame.init()

i = 0
while i < 5:
    ticks = pygame.time.get_ticks()
    print(ticks)
    i = i + 1
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running = False
#
# pygame.quit()
pygame.time.wait(1000)