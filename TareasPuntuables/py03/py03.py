

print("1.triangulo")
print("2.cuadrado")
print("3.rectangulo")
print("4.circulo")
print("5.trapecio")
print("6.paralelogramo")
print("7.rombo")
print("8.pentagono")
print("9.hexagono")



figura = int(input("Introduzca la figura geométrica: "))
match(figura):
    case 1:
        a = float(input("Introduzca el valor del lado a: "))
        b = float(input("Introduzca el valor del lado b: "))
        c = float(input("Introduzca el valor del lado c: "))
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        perimetro = a + b + c
        print(f"El área del triángulo es: {area}")
        print(f"El perímetro del triángulo es: {perimetro}")
    case 2:
        a = float(input("Introduzca el valor del lado a: "))
        area = a * a
        perimetro = 4 * a
        print(f"El área del cuadrado es: {area}")
        print(f"El perímetro del cuadrado es: {perimetro}")
    case 3:
        a = float(input("Introduzca el valor del lado a: "))
        b = float(input("Introduzca el valor del lado b: "))
        area = a * b
        perimetro = 2 * (a + b)
        print(f"El área del rectángulo es: {area}")
        print(f"El perímetro del rectángulo es: {perimetro}")
    case 4:
        r = float(input("Introduzca el valor del radio r: "))
        area = 3.1416 * r * r
        perimetro = 2 * 3.1416 * r
        print(f"El área del círculo es: {area}")
        print(f"El perímetro del círculo es: {perimetro}")
        
    case 5:
        a = float(input("Introduzca el valor del lado a: "))
        b = float(input("Introduzca el valor del lado b: "))
        c = float(input("Introduzca el valor del lado c: "))
        d = float(input("Introduzca el valor del lado d: "))
        h = float(input("Introduzca el valor de la altura h: "))
        area = ((a + b) / 2) * h
        perimetro = a + b + c + d
        print(f"El área del trapecio es: {area}")
        print(f"El perímetro del trapecio es: {perimetro}")
    case 6:
        a = float(input("Introduzca el valor del lado a: "))
        b = float(input("Introduzca el valor del lado b: "))
        h = float(input("Introduzca el valor de la altura h: "))
        area = a * h
        perimetro = 2 * (a + b)
        print(f"El área del paralelogramo es: {area}")
        print(f"El perímetro del paralelogramo es: {perimetro}")
    case 7:
        d1 = float(input("Introduzca el valor de la diagonal mayor d1: "))
        d2 = float(input("Introduzca el valor de la diagonal menor d2: "))
        a = float(input("Introduzca el valor del lado a: "))
        area = (d1 * d2) / 2
        perimetro = 4 * a
        print(f"El área del rombo es: {area}")
        print(f"El perímetro del rombo es: {perimetro}")
    case 8:
        a = float(input("Introduzca el valor del lado a: "))
        ap = float(input("Introduzca el valor del apotema ap: "))
        area = (5 * a * ap) / 2
        perimetro = 5 * a
        print(f"El área del pentágono es: {area}")
        print(f"El perímetro del pentágono es: {perimetro}")
    case 9:
        a = float(input("Introduzca el valor del lado a: "))
        ap = float(input("Introduzca el valor del apotema ap: "))
        area = (6 * a * ap) / 2
        perimetro = 6 * a
        print(f"El área del hexágono es: {area}")
        print(f"El perímetro del hexágono es: {perimetro}")
    case _:
        print("Introduce una figura")