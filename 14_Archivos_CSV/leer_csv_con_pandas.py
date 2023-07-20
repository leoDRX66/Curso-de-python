""" En cmd de windows uno el comando= "py -m pip" """
""" Para intalar pandas= "py -m pip install pandas" """
#print(type(pd)) #<class 'module'>

import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#df=dataframe son filas y columnas
#con ",names = ["name", "lastname", "age"]" agregamos un encabezado a la lista de datos
df = pd.read_csv("14_Archivos_CSV\\datos.csv", names = ["name", "lastname", "age"])
df2 = pd.read_csv("14_Archivos_CSV\\datos.csv", names = ["name", "lastname", "age"])

""" obtiene los dato de la columna nombre """
nombres = df["name"]
#print(nombres)

""" cadena = "0123456789"
print(cadena[3:6]) """

""" ordenamos el dataframe por edad """
df_edad = df.sort_values("age")
#print(df_edad)

""" odenamos de forma decendente """
df_decendente = df.sort_values("age", ascending=False)
#print(df_decendente)

""" concatenando (unir) los 2 dataframes """
df_concatenar = pd.concat([df,df2])
#print(df_concatenar)

""" accediendo a las primeras 2 fila con head() """
df_primeras_filas = df.head(2)
#print(df_primeras_filas)

""" accediendo a las ultimas 2 filas con tail() """
df_ultimas_filas = df.tail(2)
#print(df_ultimas_filas)

""" accediendo a la cantidad de filas y columnas con shape """
#es una propiedad
filas_y_columnas_totales = df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]
#print(filas_y_columnas_totales) #(4,3) 4=filas y 3=columnas

""" obteniendo data estadistica del dataframe """
df_info = df.describe()
#print(df_info)

""" accediendo a la edad de la fila 2 con loc """
elemeneto_especifico_loc = df.loc[2, "age"]
#print(elemeneto_especifico_loc)

""" accediendo a la edad de la fila 2 con iloc """
elemeneto_especifico_iloc = df.iloc[2,2]
#print(elemeneto_especifico_iloc)

""" accediendo a todas las filas de una columna """
apellidos = df.iloc[:,1]
#print(apellidos)

""" accediendo a todas las columnas de una fila """
fila_3 = df.loc[2,:]
#print(fila_3) 

""" accediendo a filas con edad mayor que 30 """
mayor_de_30 = df.loc[df["age"]>30,:]
print(mayor_de_30)

