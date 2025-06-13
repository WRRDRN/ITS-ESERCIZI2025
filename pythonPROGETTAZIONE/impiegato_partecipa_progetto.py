from __future__ import annotations
from datetime import datetime


class Impiegato:
    



    def __init__(self, nome:str,surname:str,birth:datetime,stipendio:str) -> None:
        self._nome = nome
        self._surname = surname
        self._birth = birth
        self._stipendio = stipendio
        self._progetti:list[Progetto] = []

    def nome(self) -> str:
        return self._nome
    
    def surname(self)->str:
        return self._surname
    

    def set_birth(self,birth:int)->None:
        self._birth=birth

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_surname(self,surname:str)->None:
        self._surname=surname

    def add_progetto(self,progetto:Progetto):
        self._progetti.append(progetto)

    def lista_progetti(self)->list[Progetto]:
        return self._progetti

class Partecipa:
    def partecipa(self,data_inzio:datetime):
        self.data_inizio=data_inzio
        for impiegati in Progetto:
            impiegati += 1


class Progetto:
    def progetto(self,name:str,budget:str):
        self.name=name
        self.budget=budget
        self.impiegati:list[Impiegato]=[Impiegato]
    
        


    def impiegato_su_progetto(self,impiegato:Impiegato)->None:
        self.impiegati.append(impiegato)
        impiegato.add_progetto(self)




