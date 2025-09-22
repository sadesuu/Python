num = int(input("Introduce un número: "))
lim = 0
for lim in range(1, num):
    if num % lim == 0:
        print(lim, end=" ")