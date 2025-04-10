from persona import Persona

class Studente(Persona):
        #Inizializzo un oggtto della classe studfente

        def __init__(self,name:str,surname:str,age:int,matricola:str):
            #inizializza la SUPERCLASSE,richiamando l'__init__
            super().__init__(name,surname,age)
            #scrivere il codice per inizializzare la classe Studente
            self.setMatricola(matricola)

        def setMatricola(self,matricola:str) -> None:
            #controllo se la stringa non sia vuota
            if matricola:
                self.matricola = matricola
            else:
                print("Error, cannot be nothing.")
        
        def getMatricola(self):
             return self.matricola

        #metodo che consente di visualizzare le info relative ad oggetto della classe studente,ovvero __str__
        #che ci restituisce una stringa

        def __str__(self) -> str:
             return f"Nome:{self.getName()} \nCognome: {self.getSurname()} \nMatricola: {self.getMatricola()}"

        #metodo che mi consente di calcolare la median degli esami sostenuti da uno studente:
        def getMediaEsame(self,voti_esami:list[int])-> float:
             if voti_esami:
                somma:int= 0
                for voto in voti_esami:
                    somma += voto
                    
                return round(somma/len(voti_esami),2)
             else:
                return 0.00
#metodo che stablisice se due ogetti della stessa classe sono uguali
        def __eq__(self,other)-> bool:
            #se other è None, oppure se non è istanza della classe studente
            if other is None or not isinstance(other,type(self)):
                return False
            #altrimenti valuta la seguent euguaglianza
            else:
                return self.getMatricola() == other.getMatricola()
            #due studenti sono uguali se hanno la stessa matricola 

             

             
        
