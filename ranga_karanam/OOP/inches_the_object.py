class Dimension:
    def __init__(self, inches):
        if inches < 0:
            self.feet = -1
            self.inches = -1
        else:
            self.feet = inches // 12
            self.inches = inches % 12

# Exemplos
dim = Dimension(25)
print(dim.feet)    # Output: 2
print(dim.inches)  # Output: 1

dim = Dimension(-1)
print(dim.feet)    # Output: -1
print(dim.inches)  # Output: -1
