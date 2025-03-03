# try:
#     x = 10/0
#     print(x)
# except:
#     print("Don't divisible by zero")
#
# x = lambda a, b: a **b
#
# print(x(4,4))
import matplotlib.pyplot as plt

x = [35,25,25,15]
y = ['Python', 'Javascript', 'Java', 'C#']

plt.pie(x, labels=y, autopct=f'%0.0f%%')
plt.show()