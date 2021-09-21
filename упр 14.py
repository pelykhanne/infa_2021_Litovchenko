import turtle
turtle.shape('turtle')
def star(t,n):
    for i in range (0,n):
        turtle.forward(t)
        turtle.left(180-180/n)
star(200,5)
