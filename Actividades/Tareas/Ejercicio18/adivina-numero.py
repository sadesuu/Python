import random
numero_secreto = random.randint(1, 10)
adivinado = False
intentos = 6
while intentos >1 or adivinado == False:
    intento = int(input("Adivina el número entre 1 y 10: "))
    if intento == numero_secreto:
        adivinado = True
        print("¡Felicidades! Has adivinado el número.")
    else:
        print("Número incorrecto. Intenta de nuevo.")
        intentos -=1