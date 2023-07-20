import re

texto ='''Hola maestro. estas es la cadena 1, como estas mi capitan
Estas es la linea 2. 
que onda abbb 1
Estas es la linea 2435 eh. 
que onda abbb 2
abasdfasabasdfgafsdabtryertye
Del texto
y Esta es la final (linea 3)  definitiva mi capitan'''

#"flags=re.IGNORECASE" ignora las mayusculas
#search muestra en que fila hace match
resultado0 = re.search("Hola", texto, flags=re.IGNORECASE)
#findall genera una lista de los valoraes que pida en este caso "estas"
resultado1= re.findall("estas", texto)

#\d -> busca dijitos numéricos del 0 al 9 
resultado2 = re.findall(r"\d",texto)
#\D -> busca TODO menos digitos numéricos del 0 al 9
resultado3 = re.findall(r"\D",texto)
#\w -> busca caracteres alfanuméricos [a-z, A-Z, 0-9,_]
resultado4 = re.findall(r"\w",texto)
#\W -> busca TODO menos caracteres alfanuméricos [a-z, A-Z, 0-9,_] o [espacios(' '), comas(,), parrafos(\n), parentesis('(',')')]
resultado5 = re.findall(r"\W",texto)
#\s -> busca espacios en blanco
resultado6 = re.findall(r"\s",texto)
#\S -> busca TODO menos espacios en blancos
resultado7 = re.findall(r"\S",texto)
#. -> busca TODO menos saltos en linea 
resultado8 = re.findall(r".", texto)
#\n -> busca saltos en linea
resultado9 = re.findall(r"\n", texto)
#\. -> cancelamos caracteres especiales
resultado10 = re.findall(r"\.", texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#\d(numero), \.(punto), \s(espacio)
resultado11 = re.findall(r"\d\.\s",texto)

#^ -> buscamos el comienzo de una linea y si tiene un Estas
#"flags=re.M" interpreta la busqueda como si cada entes sea un espacio en linea 
resultado12 = re.findall(r"^Estas", texto, flags=re.M)

#$ -> final de una linea
resultado13 = re.findall(r"capitan$",texto,flags=re.M)

#{n} ->Busaca n cantidad de veces el valor de la izquierda
#CONDICION = encontrame {3} veces esto \d y un espacio
resultado14 = re.findall(r"\d{3}\s",texto)

#{n,m} -> al menos n, como maximo m
resultado15 = re.findall(r"\d{1,4}",texto)
#ejemplo 2
resultado16 = re.findall(r"ab{1,3}",texto)
#ejemplo 3
resultado17 = re.findall(r"(ab){1,3}",texto)
#ejemplo 4
resultado18 = re.findall(r"[ab]{2}",texto)

print(resultado18)
