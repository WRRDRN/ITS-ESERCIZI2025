from gestioneOspedale import Persona
from typing import Self

class Dottore(Persona):
    def __init__(self, first_name:str, last_name:str,age:int,specialization:str,parcel:float):
        super().__init__(first_name, last_name,age) 
        self.specialization=specialization
        self.parcel=parcel
    
    def setSpecialization(self,specialization)->str:
        if isinstance(specialization,str):
            self.specialization=specialization
        else:
            print("La specializzazione inserita non è una stringa")


    def setParcel(self,parcel)->str:
        if isinstance(parcel,float):
            self.parcel=parcel
        else:
            print("La parcella inserita non è un float")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAvalidDoctor(self)->bool:
        if self.age >= 30:
            return "Doctor nome e cognome is valid"
        else:
            "...is not valid"

    def greet(self):
        super().greet()
        print(f"Sono un medico in {self.specialization}")
        
