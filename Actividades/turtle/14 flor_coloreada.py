import turtle as t

t.Turtle()


t.speed(100)
t.color("red")
t.begin_fill()

for _ in range(12):
    t.color("red")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.left(30)
    


t.penup()
t.goto(0,-20)
t.pendown()

t.color("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()

t.mainloop()

