try:
    width = float(input('Enter rectangugle with: '))
    length = float(input('Enter rectangugle lenth: '))

    if width == length:
        exit('That looks like a square.')

    area = width * length
    print(area)
except ValueError:
    print('Please enter a number.')