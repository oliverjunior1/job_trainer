class MotorBike:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        if self.speed - how_much >=0:
            self.speed -= how_much
        else:
            print('invalid Operation')

honda = MotorBike(50)

honda.decrease_speed(350)

print(honda.speed)
