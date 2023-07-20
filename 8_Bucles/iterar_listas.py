
#bucle for (funciona con listas y tuplas)
nombres_de_mi_familia = ["Daniela","Leandro","Franco","Candela"]
numeros = [1,4,6,7]

#La primera variable solo se ejecuta dentro del for(nombres)
for nombres in nombres_de_mi_familia:
    print(f"Los nombres de mi familia son: {nombres}")
print("--------------------")
#recoriendo la lista numeros y mutiplicandolos por 2   
for num in numeros:
    resultado = num * 2
    print(f"El doble de los numero es: {resultado}")
print("--------------------")  
#iterando 2 listas del mismo tamaño al mismo tiempo
##bucle for lista1,lista2 in zip(lista1,lista2)  
#  for nombres_de_mi_familia,numeros in zip(nombres_de_mi_familia,numeros):
    #  print(f"recorriendo lista 1: {nombres_de_mi_familia}")
    #  print(f"recorriendo lista 2: {numeros}")

#range() nos devuelve canda elemento comprendido entre los valores establecidos 
#(inicio:1) (fin:5) (resultado: 1,2,3,4)    
for num in range(1,5):
    print(num)
print("--------------------")    
for num in enumerate(numeros):
    print(num)  
print("--------------------")      
#forma de recorer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
print("--------------------")

#usando un for//else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
print("--------------------")
        