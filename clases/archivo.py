import xml.etree.ElementTree as ET
from paciente import Paciente
from lista_enlazada import ListaEnlazada

class Archivo():
    
    def __init__ (self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
    
    lista_pacientes = ListaEnlazada()

    try:
        xml_file = open("../datos.xml", encoding="utf-8")
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            lista = xml_data.findall('paciente')
            for paciente in lista:
                item_paciente = Paciente(paciente.find('datospersonales/nombre').text, paciente.find('datospersonales/edad').text)
                lista_pacientes.agregar_final(item_paciente)
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    
    lista_pacientes.recorrer_inicio()
   