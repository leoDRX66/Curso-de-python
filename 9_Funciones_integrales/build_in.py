numeros = [4,5,6,7,15,48]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

print("--------------------")

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

print("--------------------")

#redondeando a 6 decimales
numero = round(12.345487321574,6)
print(numero)

print("--------------------")

#retorna false -> 0,vacio,falso,none
#retorna true -> distinto de 0, true, cadena, dato no vacio
resultado_bool1 = bool(0)
resultado_bool2 = bool([1,2,3])
print(resultado_bool1) #false
print(resultado_bool2) #true

print("--------------------")

#retorna true -> si todos los elementos son verdaderos
resultado_all = all([1,True,[1,2,3]])
print(resultado_all)

print("--------------------")

#sumar todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)

