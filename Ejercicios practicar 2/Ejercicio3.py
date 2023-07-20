#creando una función que mustre la serie de fibonacci entre 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = []
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b
    return num
resultado = fibonacci(34)
print(resultado)



