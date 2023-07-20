
#creando una funcion simple
def saludar():
    print("Hola lea, como vas con python?")

#ejecutando la funcion simple    
saludar()

#crear una funcion que tenga parametros
def saludo(nombre,sexo):
    name = nombre.capitalize()
    genero = sexo.lower()
    if (genero == "mujer"):
        adjetivo = "reina"
    elif (genero == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "amore"
    print(f"Hola {name}, mi {adjetivo} ¿Como estas?")

saludo("camila","MuJeR")
saludo("Lean", "homBRe")
saludo("seba", "no binario")

#crear una funcion que nos retorne valores
def creando_contraseña_random(num):
    x_dijitos= "abitwrhrt6urtyjfurthffghjrtyiryd"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num + 5
    contraseña = f"{x_dijitos[c1]}{x_dijitos[c2]}{x_dijitos[c3]}{num*2}"
    #me quiero quedar con el numero q coloque
    return contraseña, num

#solo uso el primer dijito    
password, numero_dado= creando_contraseña_random(942)
print(f"Tu nueva contraseña random es: {password}")
print(f"El numero utilizado es: {numero_dado}")



