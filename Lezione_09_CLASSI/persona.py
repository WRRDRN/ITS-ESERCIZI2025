class Persona:

    '''mi servono nome, cognome, età: str,str,int'''
    # costruttore
    def __init__(self,name:str,lastname:str,age:int):
        self.name= name
        self.lastname= lastname
        self.age= age


# funzione che mostra in output i dati relativi a una persona

    def displayData(self) -> None:
        print(f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}")

        