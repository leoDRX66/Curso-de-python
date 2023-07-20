
#importo la función "def" a modulos
import saludo_en_py #namespace

saludar = saludo_en_py.Saludo("Lea")
print(saludar)

print(type(saludo_en_py)) #modulo


#Utilizo el operador "as" para asignar un nuevo nombre a el modulo utilizado
#Funciona solo en modulos de manera que ("valor" as variable)

import saludo_en_py as m_saludar

saludar1 = m_saludar.Saludo("Lean")
print(saludar1)