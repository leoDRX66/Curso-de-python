#Falto el profe y lo pibes van a arma la clase designando a un profesor(el mas grande en edad) y un asistente la mas chico

#funcion para obtener al asistente y al profesor segun la edad

def obtener_compañeros(cantidad_de_compañeros):
    
    #crear la lista de compañeros
    compañeros = []
    
    #ejecutar un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre= input("Introducir nombre: ")
        dia = int(input("Día de nacimiento: "))
        mes = int(input("Mes de nacimiento: "))
        año = int(input("Año de nacimiento: "))
        compañero = (nombre, dia, mes, año)
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordeno de ¡¡¡menor a mayor!!! segun su el tercer elemento de la lista (0,1,2,3)
    compañeros.sort(key = lambda x:x[3])
    
    #mostrar la lista
    print(compañeros) #[('lea', 4, 4, 2000), ('marta', 5, 7, 2000), ('seba', 12, 11, 2000), ('juli', 8, 12, 2001), ('nicol', 8, 4, 2004)]
    
    #compañeros[x] devuelve una tupla con (nombre, dia, mes, año) y despues accede al nombre
    #para definir al asistente y al profesor
    profesor= compañeros[0][0]
    asistente= compañeros[-1][0]
    
    #[("""nombre""",2,3,4), (1,2,3,4), (1,2,3,4), (1,2,3,4), ("""nombre""",2,3,4)]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)

print(f"El profesor es: {profesor} y su asitente es {asistente}")








