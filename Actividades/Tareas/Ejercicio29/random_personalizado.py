import random

liminf = int(input("Introduce el limite inferior: "))
limsup = int(input("Introduce el limite superior: "))


if(liminf<limsup):
    vueltas = int(input("Introduce cuantos números random quieres"))
    for i in range(vueltas):
        num = random.randint(liminf,limsup)
        print(f"Tu numero aleatorio es: {num}")
else:
        print("El limite superior tiene que ser mayor que el limite inferior")