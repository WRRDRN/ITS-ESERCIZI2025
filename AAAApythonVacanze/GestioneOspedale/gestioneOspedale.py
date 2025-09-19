class Persona:
    def __init__(self, first_name, last_name):
        self.setName(first_name)
        self.setLastName(last_name)

        if self.first_name is not None and self.last_name is not None:
            self.age = 0
        else:
            self.age = None

    def setName(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            self.first_name = None
            print("Il nome non è una stringa!")

    def setLastName(self, last_name):
        if isinstance(last_name, str):
            self.last_name = last_name
        else:
            self.last_name = None
            print("Il cognome non è una stringa!")

    def setAge(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self):
        return self.first_name

    def getLastname(self):
        return self.last_name

    def getAge(self):
        return self.age

    def greet(self):
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni!")
