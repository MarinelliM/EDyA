import csv

class Provincia:
    __pais_id : int
    __pais : str
    __provincia_id : int
    __provincia : str
    __departamento_id : int
    __departamento : str
    __sup_afectada : float
    __uni_med_id : str
    __cant_focos : int
    __ao_inicial : int

    def __init__(self, pais_id, pais, provincia_id, provincia, departamento_id, departamento, sup_afectada, uni_med_id, cant_focos, ao_inicial):
        self.__pais_id = pais_id
        self.__pais = pais
        self.__provincia_id = provincia_id
        self.__provincia = provincia
        self.__departamento_id = departamento_id
        self.__departamento = departamento
        self.__sup_afectada = sup_afectada
        self.__uni_med_id = uni_med_id
        self.__cant_focos = cant_focos
        self.__ao_inicial = ao_inicial

    def __str__(self) -> str:
        return f'[País: {self.__pais}\nProvincia: {self.__provincia}\nDepartamento: {self.__departamento}\nSuperficie Afectada: {self.__sup_afectada}\nUnidad de Medida: {self.__uni_med_id}\nCantidad de Focos: {self.__cant_focos}\nAño Inicial: {self.__ao_inicial}]'

    def get_superficie_afec(self):
        if self.__sup_afectada:
            return float(self.__sup_afectada)
        else:
            return 0.0

    def __gt__(self, otro):
        return float(self.__sup_afectada) > float(otro.get_superficie_afec())