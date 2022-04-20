
import re


class Alumno():

    def __init__(self, nombre):
        self._nombre = nombre
        

    @property
    def estudiante(self): 
        return self._nombre

    @estudiante.setter
    def estudiante(self, nombre):
        if isinstance is (nombre, str):
            self._nombre = nombre 
        else:
            print("esto no es un nombre valido")
