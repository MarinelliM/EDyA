import csv
import sys
sys.path.append(r'C:\Users\mauri\OneDrive\Documentos\Estructura de Datos y Algoritmos\Ej3_Listas\Lista_Encadenada_Contenido.py')
from Provincia import Provincia
from Lista_Encadenada_Contenido import Lista_Encadenada
class Manejador:
    __lista_provincias: Lista_Encadenada

    def __init__(self) -> None:
        self.__lista_provincias = Lista_Encadenada()

    def inicio(self):
        #with open('incendios_forestales.csv', 'r', encoding='utf-8') as archivo:
        with open(r'C:\Users\mauri\OneDrive\Documentos\Estructura de Datos y Algoritmos\Ej3_Listas\incendios_forestales.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                pais_id = int(fila[0])
                pais = fila[1]
                provincia_id = int(fila[2])
                provincia = fila[3]
                departamento_id = int(fila[4])
                departamento = fila[5]
                sup_afectada = fila[6]
                uni_med_id = str(fila[7])
                cant_focos = int(fila[8])
                ao_inicial = int(fila[9])
                provincia = Provincia(pais_id, pais, provincia_id, provincia, departamento_id, departamento, sup_afectada, uni_med_id, cant_focos, ao_inicial)
                self.__lista_provincias.insertar(provincia)

    def mostrar(self):
        return self.__lista_provincias.mostrar()

    def ordenar(self):
        return self.__lista_provincias.ordenar()

if __name__ == '__main__':
    input('Insertar:')
    a = Manejador()
    a.inicio()
    #a.mostrar()
    a.ordenar()
    a.mostrar()
