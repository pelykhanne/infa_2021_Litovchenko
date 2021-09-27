import turtle as tr
tr.penup()
tr.goto(-300,0)
tr.pendown()
x=-300
y=0
k=0.05
Ay=-10
Vx=10
Vy=80
dt=0.1
for i in range (0,1000):
    x += Vx*dt - k*Vx*dt**2/2
    Vx += -k*Vx*dt
    y += Vy*dt + (Ay-k*Vy)*dt**2/2
    Vy += (Ay-k*Vy)*dt
    if y<=0:
        Vy = -Vy
    tr.goto(x,y)
