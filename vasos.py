
class Vasos():

    def __init__(self, planta):
        #self._nombre = nombre
        self._planta = planta
        
    @property 
    def planta(self): 
        return self._planta

    @planta.setter
    def planta(self, planta):
        if isinstance(planta, str):
            self._estudiante = planta 
