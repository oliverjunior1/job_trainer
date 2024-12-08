# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('blueViolet')
timmy.backward(100)
#timmy.goto(500,0)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()