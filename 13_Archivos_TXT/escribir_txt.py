""" agregamos texto a un archivo .txt """

# no guarda la información!!!
# ",w" permiso para escribir

with open("13_Archivos_TXT\\texto_de_lea.txt","w",encoding="UTF-8") as archivo:
    #sobreescribe el archivo de texto
    ##archivo.write("JAJAJAJ la re cague")
    
    #agregando 2 lineas con writelines
    # "\n" mueve el texto a la linea de abajo
    archivo.writelines([" - Que onda master esto esta re dificil\n", " - Bob esponja\n"])
    archivo.writelines([" - Wenas como va?\n", " - Patricio\n"])