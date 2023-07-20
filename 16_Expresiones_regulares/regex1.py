import re

text = "The quick brown fox jumps over the lazy dog"

#La cadena de texto tiene que empezar con The, seguirle cualquer coaracter de espacio de linea y por ultimo tiene q terminar dog
x = re.search("^The.*dog$", text)

if x: 
    print("SI")
else:
    print("NO")