import turtle

# Crear ventana y tortuga
ventana = turtle.Screen()
ventana.bgcolor("lightblue")

t = turtle.Turtle()
t.write("Hola Mundo",
    align="center",
    font=("Arial", 24, "bold")) #mostrar un mensaje)
t.shape("turtle")
t.color("red") #color de la tortuga
#t.color(120,120,5) podemos poner el color formato RGB
t.pensize(3) #tamaño de la línea
t.pencolor("green") #color de la linea

# Dibujar un cuadrado
for _ in range(4): 
    t.forward(100) # para delante (número de pasos)
    t.left(90) # también existe right (número grados)

ventana.mainloop()

# home() vuelve a casa, centro de la ventana
# penup() home() si queremos que vuelva sin escribir línea
#clear() limpia la pantalla cuando termina
#goto(x,y) va a un punto de coordenadas específico
#shape("turtle")  “arrow”,“turtle”, “circle”, “square”,“triangle” y “classic” 
#t.screen.colormode()
#t.fillcolor()