""" Cambiar el tipo de dato de una columna """

import pandas as pd
df = pd.read_csv("Resolviendo_problemas\\datos1.csv")

""" Convertir a string los datos de una columna """
df["Edad"] = df["Edad"].astype(str)

""" Mostrar el tipo de dato del primer elemento de la columna edad """
#print(type(df["Edad"][0]))

""" Remplazando los datos "Olarte" por "Maestro" """
df["Apellido"].replace("Olarte", "Master", inplace=True)
#print(df["Apellido"])

""" Eliminar filas con datos faltantes """
df = df.dropna() #Nan no existe #(axis=1) para elinimar al columnas

""" Eliminamos las filas repetidas """
df = df.drop_duplicates()

""" Creando un CSV con el dataframe resultante (limpio)  """
df.to_csv("Resolviendo_problemas\\datos_limpios.csv")
