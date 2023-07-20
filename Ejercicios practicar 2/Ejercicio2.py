
#creemos una función que al pasarle un numero nos generenumeros primos 
#hasta llegar a ese numero

#creo una función
def es_primo(num):
    #itero una lista que tenga un rango entre 2 y el numero q yo elija-1
    #i es int 
    for i in range(2,num-1):
        #si ese numero q yo elija el resto es igual a 0 entonces no es primo 
        if num%i==0: return False
        #pero si es lo contrario returna verdadero terminando en bucle
    return True

#creamos una función q retorne una lista de los numero primos de 2 hasta el q yo elija
def primos_hasta(num):
    #creamos una lista
    primos = []
    #itero la lista en un rango entre 2 y el numero q yo elija+1
    for i in range(2,num+1):
        #verifico si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        #y lo ordenamos de menor a mayor
        if resultado == True: primos.append(i)
    #devolvemos una lista
    return primos

x=13
resultado = es_primo(x)
resultado1 = primos_hasta(x)
print(resultado)
print(resultado1)

#codigo resumido en 1 linea
primos_hastaa = lambda num1: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num1)))
print(primos_hastaa(15))