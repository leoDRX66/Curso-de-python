
#creando una lista 
lista = ["Leandro Olarte","Soy el lea", True ,float(7.6)]
print(lista[0])
print(lista[1])

#creando una tupla (NOS SE PUEDE MODIFICAR)
tupla = ("Leandro Olarte","Soy el lea", True ,float(7.6))

#esto es válido

lista[3] = "Paleta"

#esto no es válido
##tupla[3] = "Paleta"

print(tupla[3])

#creando un conjunto (set)

conjunto = {"Leandro Olarte","Soy el lea", True ,float(7.6),"Soy el lea"}

#se puede 
print(conjunto)
#nose puede acceder (no tienen un orden)
##print(conjunto[2])
###en un conjunto no puede haber datos duplicados
###no se accede a elementos por indice
print(conjunto)

#creando un diccionario (dict)(la estructura es key: value y separamos con comas)
diccionario ={
    #key : value,
    "nombre" : "Leandro Olarte",
    "edad" : int(23),
    "tengo sueño" : True,
    "altura" : float(1.82) 
}
print(diccionario["nombre"])
print(diccionario["altura"])
print(diccionario["edad"] + 10)