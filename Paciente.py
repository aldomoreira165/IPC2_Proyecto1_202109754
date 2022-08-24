from Lista import Lista

class Paciente:
    
    def __init__(self, numeroPaciente,nombre, edad, m,periodos, listaRejillasEnfermas):
        self.numeroPaciente = numeroPaciente
        self.nombre = nombre
        self.edad = edad
        self.m = m
        self.periodos = periodos
        self.listaRejillasEnfermas = listaRejillasEnfermas