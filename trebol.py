from plantas import Planta 

class Trebol(Planta):

    def __init__(self):
        self._nombre = "trebol"

    @property
    def nombre(self): 
        return self._nombre