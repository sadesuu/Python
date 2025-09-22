lim = int(input("introduzca un número"))
num1 = 0
num2 = 1
res = 0

for i in range(lim-1):
   res = num1 + num2
   num1 = num2
   num2 = res
print(f"El fibonacci es {res}")
    