def poskey(*args, **kwargs):
    print(f'Positional arguments: {args}')
    print(f'Keyward arguments: {kwargs}')

print(poskey(1,2,3,4,5,6,a=1,b=2,c=3))