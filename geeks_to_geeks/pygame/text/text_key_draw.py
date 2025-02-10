#-------------------Pygame--------------------------------------------
# import pygame
# import sys
#
# pygame.font.init()
# pygame.font.get_fonts()
#
# screen = pygame.display.set_mode((500,500))
#
# draw = pygame.draw.rect(screen, (255,0,0), (30,30,20,20))
#
# font = pygame.font.SysFont('Times New Roman', 50)
# text = font.render('Jesus is the love', True, (40,40,30,30))
# text_rect = text.get_rect()
# text_rect.center=(250,250)
#
# while True:
#     screen.blit(text, text_rect)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#             pygame.quit()
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_1:
#                 screen.fill((0,0,255))
#             elif event.key==pygame.K_2:
#                 screen.fill((0,150,120))
#     pygame.display.flip()
#
#---------------------------------Pandas--------------------------
# import pandas as pd
# import numpy as np
#
# x = np.array([1,7,9])
#
# y = pd.Series(x)
#
# print(y)
#-------------------------------tkinter--------------------------
#
# import tkinter as tk
# import tkinter as ttk
#
# from click import command
#
# root = tk.Tk()
#
# def change():
#     label2 = tk.Label(root, text='I love you Jesus').pack()
#
# label = tk.Label(root, text='Jesus is the way').pack()
# button = tk.Button(root, text='Click here').pack()
# button2 = tk.Button(root, text='Click here 2',command=change).pack()
# input = tk.Entry(root, text=' ').pack()
#
# root.mainloop()
#---------------------------matplotlib--------------------------------------
#
# import matplotlib.pyplot as plt
#
# x = [1,5,7,10,6,15,25,16]
#
# plt.plot(x)
#
# plt.show()
#---------------------------lambda----------------------------------------
# x = lambda a, b, c: a**b//c
#
# print(x(5,2,5))
#---------------------------class-----------------------------------------
# class Name:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'The name is {self.name} Oliveira and the age is {self.age} years old.'
#
# name = Name('Joao', 12)
# name1 = Name('Alyne', 38)
# name2 = Name('Mariane', 3)
#
# print(name)
# print(name1)
# print(name2)
#------------------------------
