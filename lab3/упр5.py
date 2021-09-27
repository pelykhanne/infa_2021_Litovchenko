from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(30, 70))
    unit.left(randint(0, 360))
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(10)
        if unit.xcor() < -200:
            unit.right(2*(unit.heading()-90))
        if unit.xcor() > 200:
            unit.right(2*(unit.heading()-90))
        if unit.ycor() < -200:
            unit.left(2*(180-unit.heading()))
        if unit.ycor() > 200:
            unit.left(2*(180-unit.heading()))
