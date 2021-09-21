import turtle
import math
turtle.shape('turtle')
for i in range (20,100,10):
    turtle.penup()
    turtle.goto(-i/2, -i/2)
    turtle.pendown()
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
