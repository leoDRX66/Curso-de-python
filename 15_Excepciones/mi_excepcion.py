#Crenado mi propia excepcion personalizado
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguente error: {err}")
#Lanzando mi propia exepcion
#raise MiException("JAJAJAJJA, pesona poco culta")


#manejandola        
try:
    raise MiExcepcion("JAJAJAJJA, pesona poco culta")
except:
    print("Como va a cometer ese error")
    
raise MiExcepcion("JAJAJAJJA, pesona poco culta")
    