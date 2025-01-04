class Car:
    pass


my_car = Car()
print(type(my_car))


class MyClass:
    def empty_method(self):
        pass


my_instance = MyClass()
my_instance.empty_method()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_rect = Rectangle(5, 3)
print(my_rect.area())


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(30)
print(my_account.get_balance())