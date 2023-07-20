numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#Creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#Crear una funcion que diga si es par o no
#def es_par(num):
#    if (num%2 == 0):
#        return True

#Usar filter como una funcion comun
#numeros_pares = filter(es_par, numeros)
#print(list(numeros_pares))

numeros_pares = filter(lambda numero: numero%2 == 0, numeros)
print(list(numeros_pares))


####lambda resume esta funcion 
#def multiplicar_por_dos(x):
#    return x*2