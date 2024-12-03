class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print('Calling modified protected member outside class:', self._a)

obj1 = Derived()
obj2 = Base()

print('Acessing protected member of obj1:', obj1._a)
print('Acessing protected member of obj2:', obj2._a)


