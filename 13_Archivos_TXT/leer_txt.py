""" Buscamos el archivos de texto y lo leemos """
#con print y read mostarmos lo q dice
#encoding="UTF-8" codigica todos lo caracteres volviendolos universales

archivo1 = open("13_Archivos_TXT\\texto_de_lea.txt",encoding="UTF-8")
print(archivo1.read())

# O

archivo_sin_leer = open("13_Archivos_TXT\\texto_de_lea.txt",encoding="UTF-8")
#archivo = archivo_sin_leer.read()
#print(archivo)

#Leer una linea de texto en especifico

lineas = archivo_sin_leer.readline(6) #si colocamos un numero en () nos lee la cantidad de espacios de esa linea q queramos
print(lineas)

""" Cerrar el archivo """
archivo1.close()

#ya no funciona el print
print(archivo1)