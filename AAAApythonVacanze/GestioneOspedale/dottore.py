from gestioneOspedale import Persona

class Dottore(Persona):
    def __init__(self, _first_name, _last_name):
        super().__init__(_first_name, _last_name) 

        _specialization:str|None
        _parcel:float|None
    
    

