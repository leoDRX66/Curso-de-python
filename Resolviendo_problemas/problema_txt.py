""" Tenemos 2 listas con nombre y apellido, tenemos q escribir los datos en un archivo de texto de forma optima con un for """
nombres = ["Leandro", "Matias", "Valeria", "Nicol", "Raul" ]
apellidos = ["Olarte", "Varas", "Salinas", "Ovalles", "Tarado"]

with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n")
    [arch.writelines(f"\nNombres: {n}\nApellidos: {a}\n---------------") for n,a in zip(nombres, apellidos)] #for en una linea

# es es igual===

""" for n,a in zip(nombres, apellidos):
    arch.writelines(f"\nNombres: {n}\nApellidos: {a}\n---------------") """