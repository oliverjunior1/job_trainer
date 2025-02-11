#-----------------------------------pygame---------------------------------------------
# import pygame
# import sys
#
#
# pygame.font.init()
# pygame.font.get_fonts()
#
# screen = pygame.display.set_mode((500,500))
#
# # draw
# draw = pygame.draw.rect(screen, (255,0,255), (40,40,30,30))
#
# # text
# font = pygame.font.SysFont('Times New Roman',25)
# text = font.render('Jesus is the light of the world!',True, (0,255,255))
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
#                 screen.fill((255,255,0))
#             if event.key==pygame.K_2:
#                 screen.fill((0,0,255))
#     pygame.display.flip()
#----------------------------------------matplotlib------------------------------------------
# import matplotlib.pyplot as plt
#
# x = [5,10,15,20,25,30]
# y = [25,10,27,15,35,37]
#
# plt.plot(x, y, 'o')
# plt.show()
#---------------------------------------pandas----------------------------------------------
# import pandas as pd
#
# x = pd.array([1,2,3,4,5,6])
# y =pd.Series(x)
# print(y)
#--------------------------------------lambda----------------------------------------------
# x = lambda a,b,c: a**b//c
#
# print(x(3,5,10))
#---------------------------------------class----------------------------------------------
# class Person:
#     def __init__(self, name, lname, age):
#         self.name = name
#         self.lname = lname
#         self.age = age
#     def __str__(self):
#         return f'The name is {self.name} {self.lname} and the age is {self.age} years old.'
#
# person = Person('Joao', 'Pedro', 12)
# person1 = Person('Alyne', 'Oliveira', 38)
# person2 = Person('Mariane', 'Vitória', 3)
#
# print(person)
# print(person1)
# print(person2)
#--------------------------------Time-----------------------------------------------------------
# import datetime
#
# x = datetime.datetime.now()
#
# print(x)
#--------------------------------List_comprehension---------------------------------------------
# list = [1,2,3,4,5,6,7,8,9,10]
#
# x = [a**2 for a in list]
#
# print(x)
#-----------------------------------kwars_and_args---------------------------------------------
def fum(*args):
    return sum(args)

print(fum(15,25,10,18,100))

def fum(**kwargs):
    for a, b in kwargs.items():
        return print(a, b)

fum(c=1)
fum(d=5)
fum(e=7)