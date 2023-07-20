import pandas as pd
""" Instalar en cmd (py -m pip install matplotlib) """
import matplotlib.pyplot as plt
""" Instalar en cmd (py -m pip install seaborn)"""
import seaborn as sns

df = pd.read_csv("Trabajando_con_graficos\\bigotes.csv")

""" Creando el grafico """
sns.boxplot(x="categoria", y="valor",data=df)

""" Mostrando el grafico """
plt.show()