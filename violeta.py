from plantas import Planta 

class Violeta(Planta):

    def __init__(self):
        self._nombre = "violeta"

    @property
    def nombre(self): 
        return self._nombre
        