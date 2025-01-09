#------------------------------Lambda----------------------------
# x = lambda a, b, c : a * b **c
#
# print(x(1,2,3))
#------------------------------class-----------------------------
# class Person:
#     def __init__(self, name, lname, age):
#         self.name = name
#         self.lname = lname
#         self.age = age
#
#     def __str__(self):
#         return f"The name is {self.name} {self.lname} and the age is {self.age}."
#
# p = Person("Joao", "Pedro", 12)
#
# print(p)
#----------------------------matplotlib----------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([1,2,5,7,8])
#
# plt.plot(x)
# plt.show()
#
#---------------------------args---------------------------------------------------------
# def square(*args):
#     for x in args:
#         print(x**2)
#
# square(1,2,3,4,5,6,7,8)
#
#----------------------------kwargs------------------------------------------------------
def family(**kwargs):
    for x, y in kwargs.items():
        print("%s = %s" % (x, y))

family(father = 'Joaquim', mather = 'Alyne', son = 'Joao', daughter = 'Mariane')