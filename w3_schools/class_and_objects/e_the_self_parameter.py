class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def all_name(abc):
        print(f'Hello my name is {abc.name} and my age is {abc.age} years old')

p = Person('Joao', 12)

print(p.all_name())