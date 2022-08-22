import xml.etree.ElementTree as ET
from Paciente import Paciente
from Lista import Lista

class Archivo():
    
    def __init__ (self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
    
    lista_pacientes = Lista()
    lista_posiciones_celulas_infectadas = Lista()

    try:
        xml_file = open("./datos.xml", encoding="utf-8")
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            for paciente in xml_data.findall('paciente'):
                m = (paciente.find('m').text)
                #lista_posiciones_celulas_infectadas.agregar_final(posicion)
                #item_paciente = Paciente(paciente.find('datospersonales/nombre').text, paciente.find('datospersonales/edad').text, )
                #lista_pacientes.agregar_final(item_paciente)
            for celda in xml_data.findall('paciente/rejilla/celda'):
                    x = celda.get('c')
                    y =  celda.get('f')
            
                
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    
    #lista_pacientes.recorrer_inicio()
   