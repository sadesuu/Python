empleados = {
    "50487202V":{
        "Nombre" : "Misael",
        "Puesto" : "Profesor",
        "Sueldo" : 2000
    },
    "50487203V":{
        "Nombre" : "Ana",
        "Puesto" : "Administrativa",
        "Sueldo" : 1800
    },
    "50487204V":{
        "Nombre" : "Luis",
        "Puesto" : "Conserje",
        "Sueldo" : 1200
    }

}

for i in empleados.keys():
    print(empleados.get(i).get("Nombre"))

