class Numbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

y = Numbers()
z = iter(y)

print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(f'{next(z)} é o número do azar!')
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(f'{next(z)} é Bolsonaro...')

