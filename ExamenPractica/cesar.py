def cifrado_cesar(texto, desplazamiento):
    cifrado = ""
    
    for caracter in texto:
        if caracter.isupper():
            # Para mayúsculas (A=65 en ASCII)
            cifrado += chr((ord(caracter) + desplazamiento - 65) % 26 + 65)
        elif caracter.islower():
            # Para minúsculas (a=97 en ASCII)
            cifrado += chr((ord(caracter) + desplazamiento - 97) % 26 + 97)
        else:
            # Mantener espacios y otros caracteres
            cifrado += caracter
    
    return cifrado

print(cifrado_cesar("hola", 5))

def descifrado_cesar(texto, desplazamiento):
    descifrado = ""
    
    for caracter in texto:
        if caracter.isupper():
            descifrado += chr((ord(caracter) - desplazamiento - 65) % 26 + 65)
        elif caracter.islower():
            descifrado += chr((ord(caracter) - desplazamiento - 97) % 26 + 97)
        else:
            descifrado += caracter
    
    return descifrado

print(descifrado_cesar("mtqf" , 5))