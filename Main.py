import os
from Archivo import Archivo
from Tejido import Tejido

archivo = None

#funcion para limpiar consola
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
while True:
    print("**************************")
    print("*¡Bienvenido!            *")
    print("*1. Seleccionar archivo  *")
    print("*2. Seleccionar paciente *")
    print("*3. Salir                *")
    print("**************************")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        clearConsole()
        ruta = input("Ingresa la ruta del archivo: ")
        archivo = Archivo(ruta)
        archivo.agregarArchivo()
        clearConsole()
    if opcion == 2:
        clearConsole()
        if archivo == None:
            print("No has cargado ningún archivo al sistema")
        else:
            #imprimiendo lista de pacientes
            paciente = archivo.listaPacientes.primero
            for i in range(archivo.listaPacientes.sizeOfList()):
                print(paciente.dato.numeroPaciente, paciente.dato.nombre)
                paciente = paciente.siguiente
                
            numero = int(input("Selecciona un número de paciente: "))
            pacienteSeleccionado = archivo.listaPacientes.primero
            #tomando datos de paciente seleccionado
            m = None
            periodos = None
            listaRejillasEnfermas = None
            for i in range(archivo.listaPacientes.sizeOfList()):
                if (numero == pacienteSeleccionado.dato.numeroPaciente):
                    nombre = pacienteSeleccionado.dato.nombre
                    edad = pacienteSeleccionado.dato.edad
                    m = pacienteSeleccionado.dato.m
                    periodos = pacienteSeleccionado.dato.periodos
                    listaRejillasEnfermas = pacienteSeleccionado.dato.listaRejillasEnfermas
                    #print(nombre, edad, m, periodos)
                    break
                else:
                    pacienteSeleccionado = pacienteSeleccionado.siguiente
            tejido = Tejido(m, listaRejillasEnfermas)
            tejido.generarTejido()
            tejido.contagioTejido(periodos)
            tipo, n, n1 = tejido.analizarTejidos()
            tejido.generadorXML(nombre, edad, periodos, m, tipo, n, n1)
                    
    if opcion == 3:
        print("Has salido del sistema.")
        exit()
            