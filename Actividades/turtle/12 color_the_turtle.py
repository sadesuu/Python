import turtle as t

screen = t.Screen()
screen.colormode(255)  # Usar valores RGB 0-255

turtle = t.Turtle()
turtle.speed(0)

# Gradiente en cuadrado - de azul oscuro a azul claro
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

layers = 50  # Número de capas para el gradiente
size = 200

for i in range(layers):
    # Calcular color del gradiente (azul oscuro a azul claro)
    r = int(i * 5)  # De 0 a 250
    g = int(i * 5)
    b = 255  # Mantener azul constante
    
    turtle.pencolor(r, g, b)
    turtle.fillcolor(r, g, b)
    
    # Calcular tamaño de cada capa
    current_size = size - (i * size / layers)
    
    # Centrar cada capa
    offset = (size - current_size) / 2
    turtle.penup()
    turtle.goto(-100 + offset, -100 + offset)
    turtle.pendown()
    
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(current_size)
        turtle.right(90)
    turtle.end_fill()

# Gradiente en triángulo - de amarillo a naranja
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

layers = 50
size = 200

for i in range(layers):
    # Calcular color del gradiente (amarillo a naranja)
    r = 255
    g = int(255 - i * 2.5)  # De 255 a 130
    b = 0
    
    turtle.pencolor(r, g, b)
    turtle.fillcolor(r, g, b)
    
    # Calcular tamaño de cada capa
    current_size = size - (i * size / layers)
    
    # Centrar cada capa del triángulo
    offset = (size - current_size) / 2
    turtle.penup()
    turtle.goto(-100 + offset, -100 + offset)
    turtle.pendown()
    
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(current_size)
        turtle.left(120)
    turtle.end_fill()

turtle.hideturtle()
t.mainloop()