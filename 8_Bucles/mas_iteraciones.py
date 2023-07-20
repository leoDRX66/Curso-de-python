
frutas = ["banana", "manzana", "cieruela", "pera", "naranja", "granada", "duranzo"]
cadena = "Hola Lean"
numeros = [2,3,8,10]

#evitando que se coma una manzana con la sentencia "continue"
for fruta in frutas:
    if fruta == "naranja":
       continue
    print(f"Me voy a comer un {fruta}")
print("-----------------------------------------")   
#evitar que el bucle siga ejecutandose(el else no se ejecuta)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("bucle terminado")
print("-----------------------------------------")

#recorrer un cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de código
numero_duplicados= [x*2 for x in numeros]
print(numero_duplicados)

