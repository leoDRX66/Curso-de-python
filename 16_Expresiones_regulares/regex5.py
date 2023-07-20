import re

text = "Este es un ejemplo de una página web: http://www.example.com y también podemos visitar"

# ? -> si encontras http o https mostralo igual
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)