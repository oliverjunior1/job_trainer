x = open('file.txt', 'w')

x.write('snail')
x.close()
y = open('file.txt', 'r')

print(y.read())
y.close()