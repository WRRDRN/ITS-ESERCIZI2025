class Alieno:

    def __init__(self,galaxy:str):
        self.setGalaxy(galaxy)

    def setGalaxy(self,galaxy:str)-> None:
        if galaxy:
            self.galaxy=galaxy
        else:
            print(f"Error!")

    def getGalaxy(self)-> str:
        return self.galaxy
    
    def __str__(self) -> str:
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"
    
    def speak(self)-> None:
        print(f"°éP_°ç_:éP:PéPé°:é°::P")


    
    
        
