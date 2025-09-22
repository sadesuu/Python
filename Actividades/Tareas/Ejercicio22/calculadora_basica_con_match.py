num1 = int(input("Introduzca un numero"))
num2 = int(input("Introduzca otro numero"))

operacion = input("Introduzca la operacion deseada(+, -, *, /)")

match operacion:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1 * num2)
    case '/':
        if(num1 and num2 != 0 and num1>num2):
            print(num1/num2)
        else:
            print("Error")
    
