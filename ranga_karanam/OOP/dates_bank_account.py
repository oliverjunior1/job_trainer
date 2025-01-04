class Account:
    def __init__(self, sold=0.0):
        self.sold = sold

    def deposit(self):
        value = float(input('Enter the value: '))
        if value <= 0:
            print('Invalid value')
        else:
            self.sold += value
    def show_sold(self):
        print(self.sold)
    def withdraw(self):
        value = float(input('Enter the value: '))
        if value<=self.sold and value>=0:
            self.sold -= value
        else:
            print('Invalid value or insuficient sold. ')
