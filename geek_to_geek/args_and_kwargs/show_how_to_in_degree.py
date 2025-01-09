def fun(arg1, *args):
    print('First argument: ', arg1)
    for arg in args:
        print('Argument *args: ', arg)


fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
