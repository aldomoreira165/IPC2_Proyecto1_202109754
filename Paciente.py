from Lista import Lista

class Paciente:
    
    def __init__(self, nombre, edad, m):
        self.nombre = nombre
        self.edad = edad
        self.m = m
        #self.periodos = periodos
        self.listaRegillasEnfermas = Lista()