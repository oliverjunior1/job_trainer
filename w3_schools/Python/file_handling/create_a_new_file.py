# x = open('myMessage.txt', 'x')
y = open('myMessage.txt', 'w')
y.write('Jesus is the way, the truth and the life.')
y = open('myMessage.txt', 'r')

print(y.read())

