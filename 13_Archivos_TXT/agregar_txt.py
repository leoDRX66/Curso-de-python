""" agregamos texto a un archivo .txt """

# no guarda la información!!!
# ",a" permiso para agragar, es un append

with open("13_Archivos_TXT\\texto_de_lea.txt","a",encoding="UTF-8") as archivo:
    #agregando al archivo texto
    for i in range(5):
        archivo.write(f"Linea {i+1} de JAJAJAJ la re cague\n")
    
