class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

y = Numbers()
z = iter(y)

for x in z:
    if x > 20:
        break
    else:
        print(x)


