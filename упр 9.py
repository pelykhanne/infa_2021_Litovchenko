import turtle
import math
turtle.left(90)
def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def a(r,n):
    t=2*r*math.sin(2*math.pi/(2*n))
    return t
def polygon(b,n):
    turtle.left(90-180*(n-2)/(2*n))
    for i in range (0,n):
        turtle.forward(b)
        turtle.left(180-180*(n-2)/n)
    turtle.right(90-180*(n-2)/(2*n))
for i in range (3,10):
    r=i*20
    move(r,0)
    polygon(a(r,i),i)
