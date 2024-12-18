x = open('members.txt', 'a')

x.write(input('Enter the name of the new member:'))
x.close()

x=open('members.txt', 'r')
print(x.read())
x.close()


