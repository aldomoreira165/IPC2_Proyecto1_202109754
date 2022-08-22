
class Celula: 
    
    def __init__(self, enferma, x, y, posicion):
        self.enferma = enferma
        self.x = x
        self.y = y
        self.posicion = posicion
        
    def enfermar(self):
        self.enferma = True
        
    def sanar(self):
        self.enferma = False
        
    def coordenadasCelulasVecinas(self):
        x1 = self.x - 1
        y1 = self.y - 1
        x2 = self.x
        y2 = self.y - 1 
        x3 = self.x + 1
        y3 = self.y - 1
        x4 = self.x - 1
        y4 = self.y
        x5 = self.x + 1
        y5 = self.y
        x6 = self.x - 1
        y6 = self.y + 1
        x7 = self.x
        y7 = self.y + 1
        x8 = self.x + 1
        y8 = self.y + 1
        
    def obtenerPosicionCelula(self, x, y, m):
        self.posicionCelula = (m * y) + (x + 1)
        
        