import os
from time import sleep
from Celula import Celula
from Lista import Lista
from colorama import Fore, init
import xml.etree.cElementTree as ET
import pathlib

init(autoreset=True)

class Tejido:

    def __init__(self, m, listaRejillasEnfermas):
        self.m = m
        self.listaRejillasEnfermas = listaRejillasEnfermas
        self.tejido = None
        self.tejidoSize = None
        self.listaMatrices = None
        self.tipoEnfermedad = None

        self.tejido = Lista()
        self.listaMatrices = []
        
    def ordenarLista(self):
        for i in range(self.listaRejillasEnfermas.sizeOfList()):
            actual = self.listaRejillasEnfermas.primero
            sig = actual.siguiente
            for j in range(self.listaRejillasEnfermas.sizeOfList() - 1):
                if actual.dato > sig.dato:
                    aux = actual.dato
                    actual.dato = sig.dato
                    sig.dato = aux
                actual = sig
                sig = actual.siguiente
                
    def generarTejido(self):
        self.ordenarLista()
        self.tejidoSize = 0
        lista = []
        celulaEnferma = self.listaRejillasEnfermas.primero
        for y in range(self.m):
            for x in range(self.m):
                self.tejidoSize += 1
                if self.tejidoSize == celulaEnferma.dato:
                    celula = Celula(True, x, y, self.tejidoSize)
                    self.tejido.agregar_final(celula)
                    lista.append(str(self.tejidoSize))
                    if celulaEnferma.siguiente != None:
                        celulaEnferma = celulaEnferma.siguiente
                else:
                    celula = Celula(False, x, y, self.tejidoSize)
                    self.tejido.agregar_final(celula)
        #guardando la matriz inicial
        lista = "".join(lista) 
        self.listaMatrices.append(lista)
            
    def imprimirTejido(self):
        tejido = self.tejido.primero
        for y in range(self.m):
            for x in range(self.m):
                if tejido.dato.enferma == True:
                    print(Fore.RED + "1", end=" ")
                    tejido = tejido.siguiente
                else:
                    print(Fore.GREEN + "0", end=" ")
                    tejido = tejido.siguiente
            print(" ")
            
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def contagioTejido(self, periodos):
        periodo = 0        
        print("*****PATRON INICIAL*****")
        self.imprimirTejido()
        sleep(2)
        self.clearConsole()
        for repeticion in range(periodos):
            lista = []
            periodo += 1
            listaNuevaTejido = Lista()       
            celulaActual = self.tejido.primero
            for y in range(self.m):
                for x in range(self.m):
                # condiciones para acceder a los elementos de la orilla de la rejilla
                    #rejilla en la esquina superior izquierda
                    if y == 0 and x == 0:
                        celula = self.tejido.primero
                        enferma = None
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
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion5 or celula.dato.posicion == posicion7 or celula.dato.posicion == posicion8:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                    #rejillas en la esquina superior derecha
                    elif y == 0 and x == self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x4 = x - 1
                        y4 = y     
                        x6 = x - 1
                        y6 = y + 1
                        x7 = x
                        y7 = y + 1
                        posicion4 = (self.m * y4) + (x4 + 1)
                        posicion6 = (self.m * y6) + (x6 + 1)
                        posicion7 = (self.m * y7) + (x7 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion4 or celula.dato.posicion == posicion6 or celula.dato.posicion == posicion7:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                    #regillas de primera fila y no en las esquinas
                    elif y == 0 and x != 0 and x != self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x4 = x - 1
                        y4 = y
                        x5 = x + 1
                        y5 = y
                        x6 = x - 1
                        y6 = y + 1
                        x7 = x
                        y7 = y + 1
                        x8 = x + 1
                        y8 = y + 1
                        posicion4 = (self.m * y4) + (x4 + 1)
                        posicion5 = (self.m * y5) + (x5 + 1)
                        posicion6 = (self.m * y6) + (x6 + 1)
                        posicion7 = (self.m * y7) + (x7 + 1)
                        posicion8 = (self.m * y8) + (x8 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion4 or celula.dato.posicion == posicion5 or celula.dato.posicion == posicion6 or celula.dato.posicion == posicion7 or celula.dato.posicion == posicion8:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                    #5
                    elif y == self.m - 1 and x == 0:
                        celula = self.tejido.primero
                        contador = 0
                        enferma = None
                        x2 = x
                        y2 = y - 1 
                        x3 = x + 1
                        y3 = y - 1
                        x5 = x + 1
                        y5 = y
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion3 = (self.m * y3) + (x3 + 1)
                        posicion5 = (self.m * y5) + (x5 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion2 or celula.dato.posicion == posicion3 or celula.dato.posicion == posicion5:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                        #6
                    elif y == self.m - 1 and x == self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x1 = x - 1
                        y1 = y - 1
                        x2 = x
                        y2 = y - 1
                        x4 = x - 1
                        y4 = y
                        posicion1 = (self.m * y1) + (x1 + 1)
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion4 = (self.m * y4) + (x4 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion1 or celula.dato.posicion == posicion2 or celula.dato.posicion == posicion4:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                        celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                        #7
                    elif y == self.m - 1 and x != 0 and x != self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x1 = x - 1
                        y1 = y - 1
                        x2 = x
                        y2 = y - 1
                        x3 = x + 1
                        y3 = y - 1
                        x4 = x - 1
                        y4 = y
                        x5 = x + 1
                        y5 = y
                        posicion1 = (self.m * y1) + (x1 + 1)
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion3 = (self.m * y3) + (x3 + 1)
                        posicion4 = (self.m * y4) + (x4 + 1)
                        posicion5 = (self.m * y5) + (x5 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion1 or celula.dato.posicion == posicion2 or celula.dato.posicion == posicion3 or celula.dato.posicion == posicion4 or celula.dato.posicion == posicion5:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                        #8
                    elif x == 0 and y != 0 and y != self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x2 = x
                        y2 = y - 1
                        x3 = x + 1
                        y3 = y - 1
                        x5 = x + 1
                        y5 = y
                        x7 = x
                        y7 = y + 1
                        x8 = x + 1
                        y8 = y + 1
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion3 = (self.m * y3) + (x3 + 1)
                        posicion5 = (self.m * y5) + (x5 + 1)
                        posicion7 = (self.m * y7) + (x7 + 1)
                        posicion8 = (self.m * y8) + (x8 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion2 or celula.dato.posicion == posicion3 or celula.dato.posicion == posicion5 or celula.dato.posicion == posicion7 or celula.dato.posicion == posicion8:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                        #9
                    elif x == self.m - 1 and y != 0 and y != self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x1 = x - 1
                        y1 = y - 1
                        x2 = x
                        y2 = y - 1
                        x4 = x - 1
                        y4 = y
                        x6 = x - 1
                        y6 = y + 1
                        x7 = x
                        y7 = y + 1
                        posicion1 = (self.m * y1) + (x1 + 1)
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion4 = (self.m * y4) + (x4 + 1)
                        posicion6 = (self.m * y6) + (x6 + 1)
                        posicion7 = (self.m * y7) + (x7 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion1 or celula.dato.posicion == posicion2 or celula.dato.posicion == posicion4 or celula.dato.posicion == posicion6 or celula.dato.posicion == posicion7:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
                    elif y != 0 and y != self.m - 1 and x != 0 and x != self.m - 1:
                        celula = self.tejido.primero
                        enferma = None
                        contador = 0
                        x1 = x - 1
                        y1 = y - 1
                        x2 = x
                        y2 = y - 1
                        x3 = x + 1
                        y3 = y - 1
                        x4 = x - 1
                        y4 = y
                        x5 = x + 1
                        y5 = y
                        x6 = x - 1
                        y6 = y + 1
                        x7 = x
                        y7 = y + 1
                        x8 = x + 1
                        y8 = y + 1
                        posicion1 = (self.m * y1) + (x1 + 1)
                        posicion2 = (self.m * y2) + (x2 + 1)
                        posicion3 = (self.m * y3) + (x3 + 1)
                        posicion4 = (self.m * y4) + (x4 + 1)
                        posicion5 = (self.m * y5) + (x5 + 1)
                        posicion6 = (self.m * y6) + (x6 + 1)
                        posicion7 = (self.m * y7) + (x7 + 1)
                        posicion8 = (self.m * y8) + (x8 + 1)
                        for yi in range(self.m):
                            for xi in range(self.m):
                                if celula.dato.posicion == posicion1 or celula.dato.posicion == posicion2 or celula.dato.posicion == posicion3 or celula.dato.posicion == posicion4 or celula.dato.posicion == posicion5 or celula.dato.posicion == posicion6 or celula.dato.posicion == posicion7 or celula.dato.posicion == posicion8:
                                    if celula.dato.enferma == True:
                                        contador += 1
                                        celula = celula.siguiente
                                    else:
                                        celula = celula.siguiente
                                else:
                                    celula = celula.siguiente
                        if celulaActual.dato.enferma == True:
                            if contador == 2 or contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        else:
                            if contador == 3:
                                enferma = True
                                lista.append(str(celulaActual.dato.posicion))
                            else:
                                enferma = False
                        xc = celulaActual.dato.x
                        yc = celulaActual.dato.y
                        posicion = celulaActual.dato.posicion
                        celula = Celula(enferma, xc, yc, posicion)
                        listaNuevaTejido.agregar_final(celula)
                        celulaActual = celulaActual.siguiente
            
            #generando nueva lista de tejidos
            tejidoNuevo = listaNuevaTejido.primero
            tejidoAnterior = self.tejido.primero
            for i in range(listaNuevaTejido.sizeOfList()):
                tejidoAnterior.dato.enferma = tejidoNuevo.dato.enferma
                tejidoAnterior.dato.x = tejidoNuevo.dato.x
                tejidoAnterior.dato.y = tejidoNuevo.dato.y
                tejidoAnterior.dato.posicion = tejidoNuevo.dato.posicion
                tejidoNuevo = tejidoNuevo.siguiente
                tejidoAnterior = tejidoAnterior.siguiente
                
            lista = "".join(lista) 
            self.listaMatrices.append(lista)
            
            #mostrando los periodos
            print("*********PERIODO:", periodo, "*********")
            self.imprimirTejido()
            print("*****************************")
            sleep(2)
            self.clearConsole()
            
    def analizarTejidos(self):
        size = len(self.listaMatrices)
        tipo = None
        n = None
        n1 = None
        igualesMuestraIniciaL = []
        igualesOtroPatron = []
        
        for i in range(size):
            if i > 0 and self.listaMatrices[i] == self.listaMatrices[0]:
                igualesMuestraIniciaL.append(i)
                
        for i in range(size):
            if i > 0:
                contador = 0
                actual = self.listaMatrices[i]
                for j in range(i+1, size):
                    if actual == self.listaMatrices[j] and contador == 0:
                        igualesOtroPatron.append(i)
                        contador += 1
                    
        #verificando tejidos
        if len(igualesMuestraIniciaL) >= 1:
            if igualesMuestraIniciaL[0] == 1:
                tipo = "Mortal"
            else: 
                tipo = "Grave"
        elif len(igualesOtroPatron) >= 2:
            if igualesOtroPatron[1] - igualesOtroPatron[0] == 1:
                tipo = "Mortal"
            else:
                tipo = "Grave"
        else:
            tipo = "Leve"
        
        if len(igualesMuestraIniciaL) == 0:
            n = "No se repite el patron inicial"
        else:
            n = igualesMuestraIniciaL[0]
            
        if len(igualesOtroPatron) == 0:
            n1 = "No se repite ningun patron diferente al inicial"
        else:
            n1 = igualesOtroPatron[0]
            
        return tipo, n, n1
              
    def generadorXML(self, nombre, edad, periodos, m, resultado, n, n1):
        pacientes = ET.Element("pacientes")
        paciente = ET.SubElement(pacientes, "paciente")
        datosPersonales = ET.SubElement(paciente, "datospersonales")
        ET.SubElement(datosPersonales, "nombre").text = nombre
        ET.SubElement(datosPersonales, "edad").text = str(edad)
        ET.SubElement(paciente, "periodos").text = str(periodos)
        ET.SubElement(paciente, "m").text = str(m)
        ET.SubElement(paciente, "resultado").text = str(resultado)
        ET.SubElement(paciente, "n").text = str(n)
        ET.SubElement(paciente, "n1").text = str(n1) 
        archivo = ET.ElementTree(pacientes)
        archivo.write(f" Resultados de paciente {nombre}.xml")
    
    
            
    
        
                    
                    
                    
                    
            
