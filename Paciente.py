from Lista_Matrices import ListaMatrices

class Paciente:
    
    def __init__(self, nombre, edad, casillas, periodos):
        self.nombre = nombre
        self.edad = edad
        self.casillas = casillas
        self.periodos = periodos
        self.listaMatrices = ListaMatrices()