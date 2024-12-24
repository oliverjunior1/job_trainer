# asks users to enter a password
password = input('Enter a password: ')

#returns 'Great password there' if the password has more than 7 characters
if len(password)>8:
    print('Great password there')
elif len(password)==7:
    print('Password is OK, but not too strong')
else:
    print('Your password is weak')