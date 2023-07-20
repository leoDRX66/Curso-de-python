import pandas as pd
""" Instalar en cmd (py -m pip install matplotlib) """
import matplotlib.pyplot as plt
""" Instalar en cmd (py -m pip install seaborn)"""
import seaborn as sns

df = pd.read_csv("Trabajando_con_graficos\\cofla_ingresos.csv")

""" Creando el grafico """
sns.barplot(x="fuente", y="ingresos",data=df)

""" Obteniendo el total de ingresos """
total_ingresos = df["ingresos"].sum()

""" Mostrando el total """
print(f"El total de ingresos es de: ${total_ingresos} USD")

""" Mostrando el grafico """
plt.show()