
#from: busca el mudulo 
#import: importa la funcion que yo eliga 
from saludo_en_py import Saludo

print(Saludo("Nicol"))

#Busco en el modulo y llamo a la segunda función
from saludo_en_py import Saludo_raro

print(Saludo_raro("Lea"))

#Hacemos lo mismo, pero cambiamos el nombre con el metodo "as"
from saludo_en_py import Saludo_raro as Saludo_como_coscu

saludo1=  Saludo_como_coscu("Mati")
print(saludo1)


#para ver la propiedader y metodos de el namespace
#print(dir(Saludo))

#accedemos al modulo de este nombre
#print(__name__)

#accedemos al nombre del modulo llamado
#print(Saludo.__name__)
