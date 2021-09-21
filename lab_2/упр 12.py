import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
turtle.left(90)
def arc(t):
    for i in range (0,50):
        turtle.forward(t)
        turtle.right(360/100)
for j in range (1,10):
    arc(10)
    arc(1)
