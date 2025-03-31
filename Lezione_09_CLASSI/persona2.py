class Persona:

    def __init__(self):
        self.name= ""
        self.lastname= ""
        self.age= 0


#funzione che mostra in output i dati di una persona 
    
    def displayData(self) -> None:
        print(f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}")

    #una funzione che mi consenta di impostare il valore di self.name

    def setName(self,name:str)->None:
        self.name=name
        

#un funzione che mi consenta di impostare il valore di self.lastname

    def setLastName(self, lastname:str)-> None:
        self.lastname=lastname


#una funzione che mi consenta di impostare il valore di age

    def setAge(self,age:int)-> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age 
#una funzione che mi consenta di ritornare il valore di self.mname

    def getName(self)-> str:
        return self.name
    
#funzione che mi consente di ritornare un valore di self.last name 
    def getLastName(self)-> str:
        return self.lastname
    
#una funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
        


   
