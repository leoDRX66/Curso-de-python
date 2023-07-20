""" Un paquete es una carpeta con muchos archivos python """

import paquete_carpeta

#print(type(paquete)) #modulo
print(paquete_carpeta.__path__) #Muestra la durección de el paquete


""" Busco el paquete, elijo el modulo y por ultimo la función que quiero llamar """
import paquete_carpeta.saludo

print(paquete_carpeta.saludo.Saludo("Daniela"))


""" IMPORTANTE """

#El paquete tiene q tener el __init__.py para que se considere paquete

