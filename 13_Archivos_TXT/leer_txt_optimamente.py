""" Abrir un archivo optimamente """

#abrimos el acrhivo con with open
with open("13_Archivos_TXT\\texto_de_lea.txt",encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)

#no es necesario cerrarlo con with open
    
    
