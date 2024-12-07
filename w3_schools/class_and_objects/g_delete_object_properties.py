class Person:
    def __init__(self, name,lname, age):
        self.name = name
        self.age = age
        self.lname = lname

    def all_name(self):
        print(f'The name is {self.name} and the age is {self.age}.')

p = Person('Joao', 'Oliveira', 12)

del p.lname
p.all_name()