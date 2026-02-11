import turtle as t

t.speed(100)
t.pensize(5)
t.color("old lace")
t.begin_fill()
for _ in range(4): 
    t.forward(100) 
    t.right(90)
t.end_fill()


t.color("saddle brown")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(15,-30)
t.pendown()

t.color("light cyan")
t.begin_fill()
for _ in range(4): 
    t.forward(20) 
    t.right(90)
t.end_fill()

t.penup()
t.goto(65,-30)
t.pendown()

t.color("light cyan")
t.begin_fill()
for _ in range(4): 
    t.forward(20) 
    t.right(90)
t.end_fill()


t.penup()
t.goto(65,-100)
t.pendown()


#Rectangulo puerta
t.color("saddle brown")
t.begin_fill()
t.left(180)
for _ in range(2):
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
t.end_fill()

t.mainloop()