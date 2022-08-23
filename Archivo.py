from platform import python_branch
from turtle import pos
import xml.etree.ElementTree as ET
from Paciente import Paciente
from Lista import Lista

class Archivo():
    
    def __init__ (self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
    
    lista_pacientes = Lista()
    lista_posiciones_celulas_infectadas = Lista()

    #abriendo documento xml
    try:
        xml_file = open("./datos.xml", encoding="utf-8")
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            contador = 0
            
            #obteniendo datos de paciente
            for paciente in xml_data.findall('paciente'):
                nombre = paciente.find('datospersonales/nombre').text
                edad = int(paciente.find('datospersonales/edad'))
                m = int(paciente.find('m').text)
                periodos = int(paciente.find('periodos').text)

                #obteniendo posicion de celdas contagiadas
                for celda in xml_data[contador][3]:
                    x = int(celda.get('c'))
                    y = int(celda.get('f'))
                    posicion = (m * y) + (x + 1)
                    lista_posiciones_celulas_infectadas.agregar_final(posicion)
                 
                #agregando datos al constuctor del paciente        
                item_paciente = Paciente(nombre, edad, m, periodos, lista_posiciones_celulas_infectadas)
                lista_pacientes.agregar_final(item_paciente)
                contador += 1
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()