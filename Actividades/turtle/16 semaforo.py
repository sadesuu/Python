import turtle

t = turtle.Turtle()
t.speed(100)
def circulo():
    t.circle(50)

t.color("red")
t.begin_fill()
circulo()
t.end_fill()

t.penup()
t.goto(0,-100)
t.pendown()

t.color("yellow")
t.begin_fill()
circulo()
t.end_fill()

t.penup()
t.goto(0,-200)
t.pendown()

t.color("green")
t.begin_fill()
circulo()
t.end_fill()


turtle.mainloop()