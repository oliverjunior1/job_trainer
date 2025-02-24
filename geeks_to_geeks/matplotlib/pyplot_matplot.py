import matplotlib.pyplot as plt

x = [1,7,9]
y = [15,20,25]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', label='Data Points')

ax.set_title('Basic Components of Matplotlib Figure')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

plt.show()