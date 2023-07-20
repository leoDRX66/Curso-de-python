#creandro un conjunto con set
conjunto = ["dato 1"]

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificar si es un subconjunto
resultado_sub = conjunto2.issubset(conjunto1)
resultado_sub = conjunto2 <= conjunto1
print(resultado_sub) #True

#verificar si es un superconjunto
resultado_super = conjunto1.issubset(conjunto2)
resultado_super = conjunto1 >conjunto2
print(resultado_super) #True

#verificar si hay algún número en comun(si hay solo un elemento igual = false)
numero_en_comun = conjunto1.isdisjoint(conjunto2)
print(numero_en_comun)
