import pygame
import time
import sys

pygame.init()
display_screen = pygame.display.set_mode((500,500))
text = 'Hello Guys!!'
font = pygame.font.SysFont(None, 40)
img = font.render(text, True, (255,0,0))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = pygame.Rect(rect.topright, (3,rect.height))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text) > 0:
                    text = text[:1]
            else:
                text += event.unicode

            img = font.render(text, True, (255,0,0))
            rect.size = img.get_size()
            cursor.topleft = rect.topright
    display_screen.fill((200,255,200))
    display_screen.blit(img, rect)

    if time.time() % 1 > 0.5:
        pygame.draw.rect(display_screen, (255,0,0),cursor)
        pygame.display.update()
    pygame.display.flip()