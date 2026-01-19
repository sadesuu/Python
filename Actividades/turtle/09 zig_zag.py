import turtle as t
import random
t.Turtle()
t.speed(100)



for _ in range(20):
    movimiento = random.randint(0, 200)
    direccion = random.randint(0,100)
    t.forward(movimiento)
    t.left(direccion)
t.mainloop()

