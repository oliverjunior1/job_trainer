'''Implement the Square constructor. This constructor should take an integer argument and initialize the side attribute with the value of this argument.

Implement the calculate_area() method. If the side attribute is less than or equal to zero, return -1. Otherwise, calculate and return the area of the square using the formula: side * side.

Implement the calculate_perimeter() method. If the side attribute is less than or equal to zero, return -1. Otherwise, calculate and return the perimeter of the square using the formula: 4 * side.
'''


class Square:
    def __init__(self, side):
        self.side = side
    # TODO: Initialize side with the passed value

    def calculate_area(self):
        if self.side <=0:
            return -1
        else:
            return self.side*self.side
    # TODO: Calculate and return the area of the square

    def calculate_perimeter(self):
        if self.side <=0:
            return -1
        else:
            return 4*self.side
    # TODO: Calculate and return the perimeter of the square

test1 = Square(5)
test2 = Square(0)
test3 = Square(-5)
print(test1.calculate_area(), test1.calculate_perimeter())
print(test2.calculate_area(), test2.calculate_perimeter())
print(test3.calculate_area(), test3.calculate_perimeter())


