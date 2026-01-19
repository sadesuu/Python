import turtle as t

t.Turtle()

#Dirijir la tortuga con las teclas
def arriba():
    t.forward(20)
def izquierda():
    t.left(15)
def derecha():
    t.right(15)

t.listen()
t.onkey(arriba, "Up")
t.onkey(izquierda, "Left")
t.onkey(derecha, "Right")
t.mainloop()