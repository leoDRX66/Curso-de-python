#forma no optima de sumar valores
def suma(lista):
    numero_sumados = 0
    for numero in lista:
        numero_sumados = numero_sumados + numero
    return numero_sumados

resultado = suma([1,2,3,4,5,6,7,8])
print(resultado)

#forma optima de sumar valores
def suma_total(numeross):
    return sum([*numeross])
    
resultado1 =suma_total([1,2,3,4,5,6,7,8])
print(resultado1)

#utilizando el operador * como algumento (*args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Lea",1,2,3,4,5,6,7,8)
print(resultado)



