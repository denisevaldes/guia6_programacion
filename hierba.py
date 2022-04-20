from plantas import Planta 

class Hierba(Planta):

    def __init__(self):
        self._nombre = "hierba"

    @property
    def nombre(self): 
        return self._nombre
