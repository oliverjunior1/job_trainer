def strength(password):
    if len(password) < 8:
        print('Weak Password')
    if not any(char.isupper() for char in password):
        return 'Weak Password'
    if not any(char.isdigit() for char in password):
        return 'Weak Password'
    return 'Strong Password'

print(strength(input('Enter the password: ')))

