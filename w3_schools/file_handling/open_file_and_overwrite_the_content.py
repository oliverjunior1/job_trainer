x = open('demofile3.txt', 'w')
x.write('Woops! I have deleted the content!')
x.close()

x = open('demofile3.txt', 'r')
print(x.read())