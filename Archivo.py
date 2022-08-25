import xml.etree.ElementTree as ET
from Paciente import Paciente
from Lista import Lista

class Archivo():
    
    def __init__ (self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.listaPacientes = None
    
    #abriendo documento xml
    def agregarArchivo(self):
        self.listaPacientes = Lista()
        try:
            xml_file = open(self.ruta_archivo, encoding="utf-8")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                contador = 0 #contador para asignar los datos de las celdas a cada paciente
                #obteniendo datos de paciente
                for paciente in xml_data.findall('paciente'):
                    contadorPacientes =+ 1
                    nombre = paciente.find('datospersonales/nombre').text
                    edad = int(paciente.find('datospersonales/edad').text)
                    m = int(paciente.find('m').text)
                    periodos = int(paciente.find('periodos').text)
                    
                    #obteniendo posicion de celdas contagiadas
                    listaRejillasEnfermas = Lista()
                    for celda in xml_data[contador][3]:
                        x = int(celda.get('c'))
                        y = int(celda.get('f'))
                        posicion = (m * y) + (x + 1)
                        listaRejillasEnfermas.agregar_final(posicion)
                        
                    for i in range(10000):
                        listaRejillasEnfermas.agregar_final(None)
                    
                    #agregando datos al constuctor del paciente        
                    itemPaciente = Paciente(contador, nombre, edad, m, periodos, listaRejillasEnfermas)
                    self.listaPacientes.agregar_final(itemPaciente)
                    contador += 1
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()