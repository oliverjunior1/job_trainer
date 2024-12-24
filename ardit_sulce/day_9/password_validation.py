# asks user to enter a password using an input() function
password = input('Enter a password: ')

#returns 'Great passwrod there!' if the password has more than 7 charactes.

if len(password) > 7:
    print('Great password there!')
else:
    print('Your password is weak.')