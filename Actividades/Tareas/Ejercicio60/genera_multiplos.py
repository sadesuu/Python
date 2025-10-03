num = int(input("Introduce un número: "))
n =int(input("Introduce hasta qué múltiplo quieres llegar: "))
for i in range(1, n+1):
    print(f"{num} x {i} = {num*i}")