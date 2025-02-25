import matplotlib.pyplot as plt

x = [1,5,3,7,9,12]
y = [9,10,11,12,13,14]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', label='Data Points')

ax.set_title('Basic Components of Matplotlib Figure')
ax.set_xlabel('X-label')
ax.set_ylabel('X-label')

plt.show()