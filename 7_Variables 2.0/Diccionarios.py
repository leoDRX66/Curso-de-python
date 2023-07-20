
#creando diccionario con dict()
diccionario = dict(nombre = "Leandro",apellido = "Olarte")

#{
#    "nombre": "Leando",
#    "apellido": "Olarte"
#}
print(diccionario)

#las listas no pueden ser claves(key) y usamos frozenset para meter conjuntos
diccionario={frozenset(["Hola", "Rancio"]): "jajas"}
print(diccionario)

#creando diccionarios con datos sin definir y usamos fromkeys() 
diccionario = dict.fromkeys(["nombre", "apellido", "edad"])
#creando un diccionarios cada letra lo toma como un elemento si no colocamos el "[]"
diccionario2 = dict.fromkeys("ABCDE")
#creo un diccionarios con fromkeys() cambiando el valor por defecto a "VALOR"
diccionario3 = dict.fromkeys("ABCDE", "VALOR")
print(diccionario)
print(diccionario2)
print(diccionario3)