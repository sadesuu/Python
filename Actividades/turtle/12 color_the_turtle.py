import turtle as t

t.Turtle()

t.penup()
t.goto(-100,-100)
t.pendown()

t.color("blue")
t.begin_fill()
for _ in range(4): 
    t.forward(200) # para delante (número de pasos)
    t.right(90)

t.end_fill()

t.penup()
t.goto(-100,-100)
t.pendown()

t.color("yellow")
t.begin_fill()

for _ in range(3):
    t.forward(200)
    t.left(120)

t.end_fill()
t.mainloop()