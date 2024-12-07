class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_and_age(self):
        print(f'The name is {self.name} and the age is {self.age} years old.')

p = Person("Joao", 12)

p.name_and_age()