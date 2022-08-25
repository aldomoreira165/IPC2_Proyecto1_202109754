from platform import architecture
from Celula import Celula
from Lista import Lista
from Archivo import Archivo

class Tejido:
    
    def __init__(self, m, listaRejillasEnfermas):
        self.m = m
        self.listaRejillasEnfermas = listaRejillasEnfermas
        self.tejido = None
        self.tejidoSize = None
        
        self.tejido = Lista()
             
    def generarTejido(self):
        self.tejidoSize = 0
        for y in range(self.m):
            for x in range(self.m):
                self.tejidoSize += 1
                celula = Celula(False, x, y, self.tejidoSize)
                self.tejido.agregar_final(celula)
                
    def imprimirTejido(self):
        celulaEnferma = self.listaRejillasEnfermas.primero
        tejido = self.tejido.primero
        contador = 0
        for y in range(self.m):
            for x in range(self.m):
                if tejido.dato.posicion == celulaEnferma.dato and celulaEnferma.dato != None:
                    contador += 1
                    celulaEnferma = celulaEnferma.siguiente
                    tejido = tejido.siguiente
                    print("1", end="")
                else: 
                    print("0", end="")
                    tejido = tejido.siguiente
            print(" ")
            
        
            
    