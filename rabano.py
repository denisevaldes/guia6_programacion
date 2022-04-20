from plantas import Planta 

class Rabano(Planta):

    def __init__(self):
        self._nombre = "rabano"

    @property
    def nombre(self): 
        return self._nombre
