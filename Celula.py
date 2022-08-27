
class Celula: 
    
    def __init__(self, enferma, x, y, posicion, periodo):
        self.enferma = enferma
        self.x = x
        self.y = y
        self.posicion = posicion
        self.periodo = periodo
        
    def enfermar(self):
        self.enferma = True
        
    def sanar(self):
        self.enferma = False        
        
    def obtenerPosicionCelula(self, x, y, m):
        return (m * y) + (x + 1)
        
        