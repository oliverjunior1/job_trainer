class Name:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age
    def __str__(self):
        return f'The name is {self.name} {self.lname} and the age is {self.age} years old'

name = Name('João', 'Pedro', 12)
name2 = Name('Mariane', 'Vitória', 3)
name3 = Name('Alyne','Oliveira', '39')

print(name)
print(name3)
print(name2)