alumnos = {}


def agregar_alumno(id_alumno, nombre, edad, curso):  
    alumnos.update({id_alumno : [nombre, edad, curso]})

def obtener_alumno_edad(edad):
    for i in alumnos:
        for j in alumnos[i]:
            if j == edad:
                return alumnos[i]

def eliminar_alumno_id(id_alumno):
    if id_alumno in alumnos:
        alumnos.pop(id_alumno)

def listar_alumnos():
    return alumnos

#Hola
def actualizar_alumno(id_alumno, nombre, edad, curso):
    global alumnos
    if id_alumno in alumnos:
        if nombre != "":
            alumnos[id_alumno][0] = nombre
        if edad is not None:
            alumnos[id_alumno][1] = edad
        if curso != "":
            alumnos[id_alumno][2] = curso
    
flag = True
i = 0

while flag:
    print("OPCIONES:")
    print("-------------------")
    print("1. Agregar alumno")
    print("2. Obtener alumnos por edad")
    print("3. Eliminar alumno por ID")
    print("4. Listar todos los alumnos")
    print("5. Actualizar información del alumno")
    print("6. Salir")

    listener = input("")

    match listener:
        case "1":
            id_alumno = i + 1
            i +=1
            nombre = input("Nombre del alumno: ")
            edad = int(input("Edad del alumno: "))
            curso = input("Curso del alumno: ")
            agregar_alumno(id_alumno, nombre, edad, curso)
            print("Alumno agregado exitosamente.")
        case "2":
            edad = int(input("Edad a buscar: "))
            alumnos_encontrados = obtener_alumno_edad(edad)
            print("Alumnos encontrados:", alumnos_encontrados)
        case "3":
            id_alumno = input("ID del alumno a eliminar: ")
            eliminar_alumno_id(id_alumno)
            print("Alumno eliminado exitosamente.")
        case "4":
            todos_los_alumnos = listar_alumnos()
            print("Lista de todos los alumnos:", todos_los_alumnos)
        case "5":
            id_alumno = input("ID del alumno a actualizar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            edad_input = input("Nueva edad (dejar en blanco para no cambiar): ")
            curso = input("Nuevo curso (dejar en blanco para no cambiar): ")
            edad = int(edad_input) if edad_input else None
            actualizar_alumno(id_alumno, nombre, edad, curso)
            print("Información del alumno actualizada exitosamente.")
        case 6:
            flag = False