class Elevate:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2 = num2
    def elevate(self):
        return self.num1 ** self.num2
elev = Elevate(2,3)
print(elev.elevate())