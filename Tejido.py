from platform import architecture
from re import M
from turtle import pos
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
        celulaEnferma = self.listaRejillasEnfermas.primero
        self.tejidoSize = 0
        for y in range(self.m):
            for x in range(self.m):
                self.tejidoSize += 1
                if self.tejidoSize == celulaEnferma.dato and celulaEnferma.dato != None:
                    celula = Celula(True, x, y, self.tejidoSize)
                    self.tejido.agregar_final(celula)
                    celulaEnferma = celulaEnferma.siguiente
                else:
                    celula = Celula(False, x, y, self.tejidoSize)
                    self.tejido.agregar_final(celula)

    def imprimirTejido(self):
        tejido = self.tejido.primero
        for y in range(self.m):
            for x in range(self.m):
                if tejido.dato.enferma == True:
                    print("1", end=" ")
                    tejido = tejido.siguiente
                else:
                    print("0", end=" ")
                    tejido = tejido.siguiente
            print(" ")

    def contagioTejido(self):
        celulaActual = self.tejido.primero
        # declarando vecinos
        for y in range(self.m):
            for x in range(self.m):
            # condiciones para acceder a los elementos de la orilla de la rejilla
                if y == 0 and x == 0:
                    celula = self.tejido.primero
                    contador = 0
                    x5 = x + 1
                    y5 = y
                    x7 = x
                    y7 = y + 1
                    x8 = x + 1
                    y8 = y + 1
                    posicion5 = (self.m * y5) + (x5 + 1)
                    posicion7 = (self.m * y7) + (x7 + 1)
                    posicion8 = (self.m * y8) + (x8 + 1)
                    for y in range(self.m):
                        for x in range(self.m):
                            if celula.dato.posicion == posicion5:
                                if celula.dato.enferma == True:
                                    contador += 1
                                    celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                    print("La celda 0,0 tiene ", contador)
                """elif y == 0 and x == self.m - 1:
                    celulaActual = celulaActual.siguiente
                elif y == 0 and x != 0 and x != self.m - 1:
                    celulaActual = celulaActual.siguiente
                elif y == self.m - 1 and x == 0:
                    celulaActual = celulaActual.siguiente
                elif y == self.m - 1 and x == self.m - 1:
                    celulaActual = celulaActual.siguiente
                elif y == self.m - 1 and x != 0 and x != self.m - 1:
                    celulaActual = celulaActual.siguiente
                elif x == 0 and y != 0 and y != self.m - 1:
                    celulaActual = celulaActual.siguiente
                elif x == self.m - 1 and y != 0 and y != self.m - 1:
                    celulaActual = celulaActual.siguiente
                # elementos dentro de la rejilla
                else:
                    celulaActual = celulaActual.siguiente"""
