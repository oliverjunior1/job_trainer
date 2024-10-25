# x = lambda a, b, c, d: a * b ** c - d
#
# print(x(1,2,3,4))
#-------------------------------------------------------
# The some function for the under function
# def divide(x, y):
#     return x / y
from numpy.ma.extras import average

# divide = lambda x, y: x/y
#
# print(divide(15,3))

# print((lambda x, y: x / y)(15,3))
#------------------------------------------------------
#
# def average(sequence):
#     return sum(sequence)/len(sequence)
#
# students = [
#     {'name': 'Ralf', 'grades': (67,90,95,100)},
#     {'name': 'Bob', 'grades': (56,78,80,90)},
#     {'name': 'Jen', 'grades': (98,90,95,99)},
#     {'name': 'Anne', 'grades': (100,100,95,100)}
# ]
#
# for student in students:
#     print(average(student['grades']))

average = lambda sequence: sum(sequence)/len(sequence)

students = [
    {'name': 'Ralf', 'grades': (67,90,95,100)},
    {'name': 'Bob', 'grades': (56,78,80,90)},
    {'name': 'Jen', 'grades': (98,90,95,99)},
    {'name': 'Anne', 'grades': (100,100,95,100)}
]

for student in students:
    print(average(student['grades']))