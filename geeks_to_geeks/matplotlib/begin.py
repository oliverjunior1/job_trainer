# import matplotlib.pyplot as plt
#
# x = [1,5,7]
# y = [3,4,5]
#
# plt.title('Line 1', color='red')
# plt.plot(x,y)
# plt.show()
#------------------------------------------------
#
# import matplotlib.pyplot as plt
#
# x = [1,3,4,2,7,6,10]
# y = [15,20,25,30,35,40,45]
#
# plt.bar(x,y)
# plt.title('Bar Chart')
#
# plt.legend(['bar'])
# plt.show()
#-------------------------------------------------
import matplotlib.pyplot as plt

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]

plt.scatter(x, y)
plt.legend('A')

plt.title('Scatter chart')
plt.show()