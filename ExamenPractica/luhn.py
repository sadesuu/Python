def luhn_check(numero):
    if not numero.isdigit():
        return False
    
    digitos = [int(d) for d in numero][::-1]
    impares = digitos[0::2] #Posición en indice par
    pares = digitos[1::2] #Posición en indice impar
    print(digitos)
    print(impares)
    print(pares)
    suma_total = sum(impares) #Suma los numeros que no necesitan ser duplicados
    

    for d in pares: #Recorre los numeros de posicion impar
        duplicado = d * 2 #Los multiplica * 2
        suma_total += duplicado if duplicado < 10 else duplicado - 9 #Si la multiplicacion no es mayor a 10 los suma directamente sino le resta 9
    print(suma_total)
    return suma_total % 10 == 0 #Comprueba que sea valido ya que tiene que dar resto 0 al dividir la suma total por 10

# Prueba

print(luhn_check("4532015112830341"))  # True
print(luhn_check("1234567890"))        # False
