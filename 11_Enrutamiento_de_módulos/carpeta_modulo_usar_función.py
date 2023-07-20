
""" Dos formas de llamar al modulo dentro de una carpeta """

#1)
from funciones_buenas.saludo_en_py import Saludo
saludar = Saludo("Leandro")
print(saludar)

#2)
import funciones_buenas.saludo_en_py

print(funciones_buenas.saludo_en_py.Saludo("Lucas"))

""" Importar con sys """ 
#print(sys.builtin_module_names) "nos da todos los valores las propiedades como sys"
#print(sys.path) "nos dice cual es la ruta actual"

import sys
sys.path.append('c:\\Users\\Mega Tecnologia\\Desktop\\Curso de python\\ejemplo_de_enrutamiento\\funciones_buenas')

