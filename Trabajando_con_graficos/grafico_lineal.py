import pandas as pd
""" Instalar en cmd (py -m pip install matplotlib) """
import matplotlib.pyplot as plt
""" Instalar en cmd (py -m pip install seaborn) """
import seaborn as sns

df = pd.read_csv("Trabajando_con_graficos\\pedos.csv")

""" Creando el grafico """
sns.lineplot(x="fecha", y="pedos",data=df)

""" Creando un punto en el momento de mas pedos """
plt.plot("01-09",17,"o")

""" Mostrando el grafico """
plt.show()