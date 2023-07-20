diccionario = {
    "nombre" : "Leandro",
    "apellido" : "Olarte",
    "edad" : 23
}

#Usamos for para que el diccionario nos devuelva una tumpla 
for key in diccionario.items():
    print(key)
    
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor: {value}")