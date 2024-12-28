def strenght(password):
    isUpper = False
    isDigit = False
    isMoreThanEight = False

    for x in password:
        if x.isupper():
            isUpper == True
        if x.isdigit():
            isDigit == True
        if len(x) >= 8:
            isMoreThanEight == True

    if isUpper == True and isDigit == True and isMoreThanEight == True:
        print('Strong Password')
    else:
        print('Weak Password')

strenght(input('Input your password: '))
