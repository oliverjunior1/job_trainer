# x = lambda a, b: a**b
# print(x(5,5))
#---------------------luck------------------------------------
# import random
#
# def lucky():
#     x = random.sample(range(1,61),6)
#     return sorted(x)
#
# y = lucky()
# print(y)
#-------------------simple-if-else----------------------------
# x = 20
#
# print("You can't drive.") if x < 18 else print("You can drive.")
#----------------------try-except------------------------------
# try:
#     x=10/0
#     print(x)
# except:
#     print("You can't divide a number to zero!")
#-------------------------extend-and-reverse-----------------------------------
x = [1,2,3,4]
y = [5,6,7,8]

x.extend(y)
x.sort(reverse=True)

print(x)

