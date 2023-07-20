
#Creando una frase de 3 parametros
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keyword arguments (argumentos de palabra clave)
frase_completa = frase(adjetivo = "capo", nombre = "Leandro", apellido = "Olarte" )
print(frase_completa)

#Creando la misma frase pero mas reducida
def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_completa1 = frase("Leandro", "Olarte", "inteligente" )
print(frase_completa1)