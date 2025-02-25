import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'Javascript']
sizes = [40,30,20,10]
plt.pie(sizes, labels=labels, autopct='%0.0f%%')
plt.show()