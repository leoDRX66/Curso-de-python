
#creandro una lista con list([])
lista = list(["Hola","soy",32,34,36,"Leandro"])
lista0 = list([52,105,48, 96, 1, 74, True, False,])
lista1 = list(["Hola","soy",32,34,36,"Leandro"])
#devuelve la cantidad de elementos de una lista
cantidad_de_elementos = len(lista)

#agregando elementos a la lista
agregando_con_append = lista.append("JAJAJAJ")

#agragando un elemento a la lista en un lugar especificado
##Ejemplo 0, 1, "Q" (indice 2)
agregando_con_inster = lista.insert(2,"Q")

#agregando varios elementos a la lista
##le estamos parando una lista a la lista original
agregando_con_extend = lista. extend([False,2023])

#eliminando un elemneto de la lista por su indice
##es distindo si ponemos eliminar_elemento_de_la_lista = lista.pop(0)
###me va a mostrar lo q elimino

lista.pop(0) #elimina "Hola"
lista.pop(-1) #(-1) elimina el ultimo elemento

#remueve un elemneto de la lista por su nombre
lista.remove("Leandro") #quita "Leandro"

#remueve todos los elemntos de la lista
#####lista.clear()""

#si usamos "sort()" odenamos la lista siempre q sean numero o True y False de mayor a menor
#lista0.sort(reverse=True) #lo ordena de mayor a menor 
lista0.sort()

#invierte los elementos sean numeros o textos
lista1.reverse()

print(lista)
print(lista0)
print(lista1)
#rint(dir(("QUE ONDA", 23))) TUPLA

encontra_la_posicion_de_elemento = lista0.index(52) #4ta posicion segun lo q modifique arriba
 
print(encontra_la_posicion_de_elemento)