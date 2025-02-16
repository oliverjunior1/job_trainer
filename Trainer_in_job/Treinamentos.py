#---------------------------lambda------------------------------------------
# x = lambda a, b: a**b
#
# print(x(5,4))
#---------------------------List_Comprehension------------------------------
# x = [1,2,3,4,5,6,7,8]
#
# x_2 = [a**2 for a in x]
#
# print(x_2)
#---------------------------------------------------------------------------
# fruits = ['apple', 'melon', 'pineapple', 'lemon']
#
# fruits_a = [x for x in fruits if 'a' in x]
#
# print(fruits_a)
#----------------------------class------------------------------------------
# class Bless:
#     def __init__(self, name, age, life ):
#         self.name = name
#         self.age = age
#         self.life = life
#
#     def __str__(self):
#         return f'God, bless {self.name} who has {self.age}, the {self.life} area, in the name of Jesus!'
#
# bless = Bless('Joao Pedro', 12, 'Health')
# bless2 = Bless('Mariane Vitoria', 3, 'Health')
#
# print(bless)
# print(bless2)
#--------------------------------Tkinter---------------------------------------
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry('500x500')
# label = tk.Label(root, text='Jesus is the light of the world!')
# label.pack()
# def text():
#     label = tk.Label(root, text='How I love You my Lord Jesus!').pack()
# button = tk.Button(root, text='CLick here', command=text)
# button.pack()
# root.mainloop()
#--------------------------------Pygame----------------------------------------
# import pygame
# import sys
#
# pygame.font.init()
# pygame.font.get_fonts()
#
# screen = pygame.display.set_mode((500,500))
#
# # draw
# draw = pygame.draw.rect(screen, 'lightblue', (40,40,30,30))
#
# # text
# font = pygame.font.SysFont('Times New Roman', 25)
# text = font.render('Jesus is in the door and knock!', True, 'yellow')
# text_rect = text.get_rect()
# text_rect.center=(250,250)
#
# # finish
# while True:
#     screen.blit(text, text_rect)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#             pygame.quit()
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_1:
#                 screen.fill('pink')
#                 draw = pygame.draw.rect(screen, 'red', (200,200,30,60))
#             if event.key == pygame.K_2:
#                 screen.fill('light green')
#                 draw = pygame.draw.rect(screen, 'orange', (100, 100, 30, 60))
#
#     pygame.display.flip()
#----------------------------matplotlib--------------------------------------------
# import matplotlib.pyplot as plt
#
# x = [1,7,3,11,12,9,15]
#
# plt.plot(x)
#
# plt.show()
#------------------------------pandas---------------------------------------------
# import pandas as pd
#
# x = pd.array([5,1,7,3])
# y =pd.Series(x)
#
# print(y)
#------------------------------pandas-matplotlib-----------------------------------
# import matplotlib.pyplot as plt
# import pandas as pd
#
# x = pd.array([1,7,5,11])
# y = pd.Series(x)
#
# plt.plot(y)
#
# plt.show()
#----------------------------------pygames_new------------------------------------
# list

mylist = [1,2,3,4,5]
print(type(mylist))
print(mylist)

# tupple
mytupple = (1,2,3,4,5,6)
print(type(mytupple))
print(mytupple)

# set
myset = {1,2,3,4,5}
print(type(myset))
print(myset)

# dict
mydict = {'name':'Alyne', 'age':18, 'name': 'Joaquim', 'age':42 }
print(type(mydict))
print(mydict)
