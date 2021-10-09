import turtle
from random import choice
from turtle import Turtle, Screen

turtle.colormode(255)


color_list = [(222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

timmy = Turtle()
timmy.shape("turtle")
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
timmy.setx(-300)
timmy.sety(-300)

counter = 0
pos_y = -300
print(timmy.pos())


while counter != 10:
    for _ in range(10):
        dor_col = choice(color_list)
        timmy.dot(20, dor_col)
        timmy.forward(50)
    pos_y += 50
    timmy.setx(-300)
    timmy.sety(pos_y)
    counter += 1


screen = Screen()
screen.exitonclick()