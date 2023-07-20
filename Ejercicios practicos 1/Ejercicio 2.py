
#1)Perdile al usuario que diga cualquier texto
texto =input("Introduce un texto cualquiera y te digo el tiempo q tardaste en decirlo: ")

#split("") separa las palabras
palabras_separadas = texto.split(" ")
#len() cuenta la cantidad de elementos
cantidad_de_palabras = len(palabras_separadas)
#2 palabras por minuto
tiempo_en_decir = cantidad_de_palabras / 2

print(f"Tu escribiste {cantidad_de_palabras} palabras.")

if tiempo_en_decir <= 5:
    print("Hablas de manera normal ")
else:
    print("¡¡¡Para flaco tampoco te pedi un testamento!!!")
    
    

print(f"Si dices {texto} tardarias en decrilo {tiempo_en_decir} segundos.")
print(f"Y dalto tardaria {round(10-(tiempo_en_decir * 0.3), 1)} % más rapido en decirlo. ")
print(f"Dalto en segundos tardaria {round(tiempo_en_decir * (tiempo_en_decir * 0.3), 2)}")



