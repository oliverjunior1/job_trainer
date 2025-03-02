import random

def lucky():
    x = random.sample(range(1,25),15)
    return sorted(x)

y = lucky()
print(y)