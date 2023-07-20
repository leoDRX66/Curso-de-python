diccionario ={
    "nombre" : "Leandro",
    "apellido" : "Olarte",
    "edad" : 23,
    "altura" : float(1.82)
}

#devuelve las keys ("""key""" : "value",)
claves = diccionario.keys()

#devuelve el valor ("key" : """value""",)
valores = diccionario.get("apellido")

#elimina todos los elementos del diccionario
#####eliminar = diccionario.clear()

#eliminando un elemento del diccionario
eliminar_elementos = diccionario.pop("edad")

#devuelve el diccionario completo ("key" : "value",)
##lo itero (recorro el elemento)
diccionario_completo = diccionario.items()

print(claves)
print(valores)
print(eliminar_elementos)
print(diccionario_completo)
#####print(eliminar) #no queda nada
