import turtle
turtle.shape('turtle')
turtle.left(90)
def circlel(t):
    for i in range (0,100):
        turtle.forward(t)
        turtle.left(360/100)
def circler(t):
    for i in range (0,100):
        turtle.forward(t)
        turtle.right(360/100)
for j in range (1,10):
    circlel(j)
    circler(j)
