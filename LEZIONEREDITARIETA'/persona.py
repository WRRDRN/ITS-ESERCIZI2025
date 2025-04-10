class Persona:
    def __init__(self, name,surname,age):
        self.setName(name)
        self.setSurname(surname)
        self.setAge(age) 

    def __str__(self) -> str:
        return (f'Nome: {self.name} \nCognome: {self.surname} \nEtà: {self.age}')
    

    def setName(self,name):
        self.name=name

    def getName(self):
            return self.name
    

    
    def setSurname(self,surname):
        self.surname=surname

    def getSurname(self):
            return self.surname
    


    def setAge(self,age):
        if age < 0 or age > 130:
            self.age= 0
        else:
            self.age = age

    def getAge (self):
        return self.age
    

istanza_di = Persona("Adriano","Morra",28)

print(istanza_di)
    







    