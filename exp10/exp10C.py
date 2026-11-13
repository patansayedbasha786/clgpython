import turtle
t = turtle.Turtle()
def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)
def rectangle():
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)
def polygon():
    n = int(input("Enter number of sides: "))
    for i in range(n):
        t.forward(80)
        t.left(360 / n)
def circle():
    t.circle(50)
def square():
    for i in range(4):
        t.forward(100)
        t.left(90)
triangle()
t.penup()
t.goto(150, 0)
t.pendown()
rectangle()
t.penup()
t.goto(-150, -150)
t.pendown()
polygon()
t.penup()
t.goto(150, -150)
t.pendown()
circle()
t.penup()
t.goto(0, -250)
t.pendown()
square()
turtle.done()
