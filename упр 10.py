import turtle
turtle.shape('turtle')
def circlel(t):
    for i in range (0,100):
        turtle.forward(t)
        turtle.left(360/100)
def circler(t):
    for i in range (0,100):
        turtle.forward(t)
        turtle.right(360/100)
for j in range (0,12):
    circlel(1)
    circler(1)
    turtle.left(360/12)
