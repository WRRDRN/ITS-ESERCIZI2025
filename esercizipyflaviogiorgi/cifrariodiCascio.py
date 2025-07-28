from abc import ABC,abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self,testoinchiaro:str)->str:
        pass
    
class DecodificareMessaggio(CodificatoreMessaggio):
    @abstractmethod
    def decodifica(self,testocodificato:str):
        pass
    
class CifratoreAScorrimento(CodificatoreMessaggio,DecodificareMessaggio):

    def __init__(self,chiave:int):
        self.chiave=chiave

    def codifica(self,testoinchiaro:str)->str:
        risultato= ""
        for el in testoinchiaro:
            if el.isalpha():
                



    

