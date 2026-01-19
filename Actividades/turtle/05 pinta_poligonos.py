import turtle

lados = int(input("Introduce el número de lados: "))

angulo = 360/lados

t = turtle.Turtle()

for _ in range(lados):
    t.forward(80)
    t.left(angulo)

turtle.mainloop()