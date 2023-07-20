import re

text = "remplazando todas las vocales por el asteriscos"

#busca todas las vocales por separado y las reemplaza por *
new_text = re.sub("[aeiou]","*",text)

print(new_text)