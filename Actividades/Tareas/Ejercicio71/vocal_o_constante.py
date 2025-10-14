letra = input("Introduzca una letra: ").lower()

match letra: 
    case "a" | "e" | "i" | "o" | "u":
        print("Es una vocal")
    case "@" | " #" | "$" | "%" | "&" | "!" | "¡" | "¿" | "?":
        print("Es un caracter especial")
    case _:
        print("Es una consonante")