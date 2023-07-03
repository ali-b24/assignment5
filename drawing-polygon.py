import turtle

t=turtle.Pen()
t.speed(2)
t.shape('turtle')
t.goto(0,0)
x=50
y=-50
for i in range (10):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for j in range(i+3):
        t.left(360/(i+3))
        t.forward(100)

    x=x+0.1
    y=y-10
    t.penup()
    t.goto(x,y)
    t.pendown()   
