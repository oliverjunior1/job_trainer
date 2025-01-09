# def myFun(*argv):
#     for arg in argv:
#         print(arg)
#
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def mult(*args):
    for arg in args:
        print(arg**2)

mult(1,2,3,4,5,6)
