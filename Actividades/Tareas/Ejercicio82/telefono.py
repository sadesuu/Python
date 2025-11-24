telefonos = {
    "Ana": "555-1234",
    "Luis": "555-5678",
    "María": "555-9012",
    "Carlos": "555-3456",
    "Sofía": "555-7890"
}


buscarNombre = input("Introduzca el nombre que desea buscaar: ")

if telefonos.__contains__(buscarNombre):
    print(f"Telefono de {buscarNombre} es: {telefonos.get(buscarNombre)}")
else:
    print("Usuario no encontrado")