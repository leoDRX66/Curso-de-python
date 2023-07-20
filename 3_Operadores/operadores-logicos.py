
#AND (solo si todo es True es true)

Resultado0 = True & True #Devolver True
Resultado1 = False & True #Devolver False    
Resultado2 = True & False #Devolver False 
Resultado3 = False & False #Devolver False 

#OR (si uno de ellos es true entonces es true)

Resultado4 = True | True #Devolver True 
Resultado5 = False | True #Devolver True 
Resultado6 = True | False #Devolver True 
Resultado7 = False | False #Devolver False 

#NOT (niega el siguiente)

Resultado8 = not True #Devolver False 
Resultado9 = not False #Devolver True 

ejemplo = not 5 < 20 #Devolver False

print(ejemplo)