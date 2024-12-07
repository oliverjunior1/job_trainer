class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def all_name(self):
        print(f'The name is {self.name} and the age is {self.age}.')

p = Person('Joao', 11)

#delete p.age

p.all_name()