import turtle

t = turtle.Turtle()

t.color("black")

for _ in range(4):
    t.forward(200)
    t.left(90)


t.penup()
t.goto(-200,0)
t.pendown()

t.color("red")
t.begin_fill()

for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

t.penup()
t.goto(200,0)
t.pendown()

t.color("red")
t.begin_fill()

for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()


turtle.mainloop()