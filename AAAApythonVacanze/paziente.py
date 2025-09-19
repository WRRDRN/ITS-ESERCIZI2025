from typing import Self
from gestioneOspedale import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name,age,idCode):
        super().__init__(first_name, last_name,age)
        self.idCode=idCode

    def setIdCode(self,idCode:str):
        self.idCode=idCode
    
    def getIdCode(self):
        return self
    
    def patientInfo(self)->str:
        return f'Paziente:{self.first_name} {self.last_name} | ID: {self.idCode}'