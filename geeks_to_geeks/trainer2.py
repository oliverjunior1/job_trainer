# import tkinter as tk
# import random
#
# root = tk.Tk()
# root.geometry(('1300x200'))
# def megasena():
#     x = random.sample(range(1,61), 6)
#     sorted(x)
#     return label.config(text=f'The numbers of megasena are: {sorted(x)}')
# def lotofacil():
#     x = random.sample(range(1,25), 15)
#     sorted(x)
#     return label.config(text=f'The numbers of megasena are: {sorted(x)}')
#
# label = tk.Label(root, text="João 14:13-14. Nessa passagem, Jesus diz que fará tudo o que for pedido em seu nome para que o Pai seja glorificado no Filho. A passagem também diz que aquele que crê em Jesus fará as obras que ele faz e fará ainda maiores do que essas")
# label.pack()
# button1 = tk.Button(root, text='Click here to megasena', command=megasena)
# button1.pack()
# button2 = tk.Button(root, text='Click here to megasena', command=lotofacil)
# button2.pack()
# tk.mainloop()

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'red', (250,200,50,30))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the world!', True, 'white')
text_rect = text.get_rect()
text_rect.center=(250,100)

while sys:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
