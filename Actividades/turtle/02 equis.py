import turtle

t = turtle.Turtle()

t.left(45)
#Crear una "X" con turtle
for _ in range(4):
    t.left(90)
    t.forward(200)
    t.goto(0,0)