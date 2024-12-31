class Motorbike:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f'The motorcicle {self.name} speed to {self.speed}.'

honda = Motorbike('Honda', 120)
suzuki = Motorbike('Suzuki', 119)

print(honda)
print(suzuki)
