import turtle
tao = turtle.Pen()
tao.shape('turtle')
def rectangle():
    for i in range(6):
        tao.fd(100)
        tao.left(60)

rectangle()
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

rectangle()
Go(45,45)
rectangle()
Go(-90,-90)
rectangle()
Go(-45,-45)
rectangle()
