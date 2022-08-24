from Celula import Celula
from Lista import Lista

class Tejido:
    
    def __init__(self, m):
        self.m = m
        
    def generarMuestraInicial(self):
        arreglo = [10, 50, 85]
        posicion = 0
        respuesta = False
        for filas in range(self.m):
            for columnas in range(self.m):
                posicion += 1
                for i in range(len(arreglo)):
                    if posicion == arreglo[i]:
                        print("1", end=" ")
                        respuesta = True
                        break
                if respuesta == False:
                    print("0", end=" ")
                respuesta = False
            print("")
                
    