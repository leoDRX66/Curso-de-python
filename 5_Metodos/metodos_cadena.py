cadena1 = "Hola soy Leandro"
cadena2 = "bienvenido a python"
cadena3 = "Mido 1.82 metros"
cadena4 = "23"
cadena5 = "HolasoyLeandro"

#Pone todo en mayuscula (upper)
mayuscula = cadena1.upper()

#Pone todo en minuscula (lower)
minuscula = cadena2.lower()

#Primer letra en mayuscula (capitalize)
primera_letra_en_mayuscula = cadena2.capitalize()

#Buscar un valor que le pidamos
##Nos da la pocision de 0 a infinito
###Si no encuentra el valor nos da (-1)
####Los espacios cuentan como numeros 
busqueda_find = cadena1.find("H")

#Buscamos una cadena en otra cadena
##Si no encuentra un valor nos da una excepcion (error)
busqueda_index = cadena1.index("a")

#Si es numerico devuelve true, sino devolvemos false
busqueda_numero = cadena4.isnumeric()

#Si es alfanumerico devolvemos true, sino devolvemos false
##Los espacios son caracteres especiales
busqueda_aflanumerico = cadena5.isalpha()

#Devuelve el número(N) de ocurrencias de una subcadena en la cadena dada.
##Si no hay cuenta cero(0) veces
contar_coincidencia = cadena1.count("a") #hay 2 a 

#Contamos cuantos caracateres tiene una cadena 
#Es una funcion len()
contar_caracteres = len(cadena1) #16

#Verifica si una cadena empieza con una letra o palabra que nosotros designemos
empieza_con = cadena1.startswith("H") #True

#verifica si una cadena termina con una letra o palabra que nosotros desiganemos
termina_con = cadena2.endswith("n")

#Nos remplaza un pesazo de la cadena
#Si no encuenta coincidencia no remplaza nada 
cadena_nueva = cadena1.replace("Hola","Olu")

#Separa por el parametro dado
##Este metodo me da una lista []
separar_cadena = cadena3.split(" ")


print(separar_cadena)
print(separar_cadena[0])