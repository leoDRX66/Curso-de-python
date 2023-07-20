#creando funcion que suma numeros
def suma_dos():
    #iniciando bucle
    while True:
        #poniendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una exepción, pedirle que reingrese los datos
        except ValueError as e:
            print("Te pedi un numero salame no te hagas el gracioso")
            print(f"ERROR: {type(e).__name__}")
        #si todo sale bien terminamos el bucle  
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("Manejo de exepción finalizado")
    
    #mostrando el resultado
    return resultado

print(suma_dos())