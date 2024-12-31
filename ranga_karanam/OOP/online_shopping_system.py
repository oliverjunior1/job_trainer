
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def login(self):
        return f'You make your login {self.name}.'

    def logout(self):
        return f'You make your logout {self.name}'

class Product:
    def __init__(self, name, price, quantity_available):
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def order(self):
        if self.quantity_available < 0:
            print('Unavailable product')
        else:
            products= int(input('Enter how much product do you want: '))
            if products > self.quantity_available:
                print('Insuficiently products.')
            else:
                print(f'You aquired {products}.')
x = ''
items = []
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def addItem(self):
        x = self.items.append(input('Add an Item: '))
    def removeItem(self):
        x = self.items.remove(input('remove an Item'))


