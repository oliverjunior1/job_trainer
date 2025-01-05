class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def invert(self):
        self.red = 255 - self.red
        self.green = 255 - self.green
        self.blue = 255 - self.blue

color = RGBColor(255,0,0)
color.invert()
print(color.red)
print(color.green)
print(color.blue)
