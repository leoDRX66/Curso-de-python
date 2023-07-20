import re 

# La cadena en la que se buscarán los patrones
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

# El patrón a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se remplazará el patrón
replacement = "fecha oculta"

# Reemplazar todas las apariciones del patrón en la cadana de texto
new_text = re.sub(pattern, replacement, text)

# Imprimir el resultado
print("Texto modificado:", new_text)

""" Texto modificado: La fecha es Fecha oculta 
y el teléfono es +1-555-555-5555 """
