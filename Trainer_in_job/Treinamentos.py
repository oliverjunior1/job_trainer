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
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,5,7,8])

plt.plot(x)
plt.show()