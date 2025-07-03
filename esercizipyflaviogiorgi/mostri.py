import random

class Creatura:
    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.nome = nome
        else:
            self.nome = "Creatura Generica"
    
    def getNome(self) -> str:
        return self.nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.nome}"

class Alieno(Creatura):
    def __init__(self):
        self._setMatricola()
        self._setMunizioni()

        nome = f"Robot-{self._matricola}"

        if not nome.startswith("Robot-") or not nome[6:].isdigit():
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome = f"Robot-{self._matricola}"

        super().__init__(nome)

    def _setMatricola(self):
        self._matricola = random.randint(10000, 90000)

    def getMatricola(self):
        return self._matricola

    def _setMunizioni(self):
        self._ammo = [i * i for i in range(15)]

    def getMunizioni(self):
        return self._ammo

    def __str__(self):
        return f"Alieno: {self.nome}"


class Mostro(Creatura):

    def __init__(self, nome:str, urlo_vittoria:str, gemito_sconfitta:str):
        super().__init__(nome)                 
        self._setVittoria(urlo_vittoria)      
        self._setSconfitta(gemito_sconfitta)  
        self._setAssalto()                    



    def _setVittoria(self,vittoria:str)->str:
        if isinstance(vittoria,str) and vittoria.strip():
            self.vittoria=vittoria
            return "GRAHHHHH"
    
    def getVittoria(self)->str:
        return self.vittoria
    
    def _setSconfitta(self,gemito:str)->str:
        if isinstance(gemito,str) and gemito.strip():
            self.gemito=gemito
            return "UUUuurghhhh"
        
    def getSconfitta(self)->str:
        return self.gemito
    
    def _setAssalto(self)->list:
        self.assalto=[]
        x=random.sample(range(1,100),15)
        self.assalto.append(x) 


    def getAssalto(self)->list:
        return self.assalto       

    def __str__(self):
        nome_mostro= ""
        for i in range(len(self.nome)):
            if i % 2 ==0:
                nome_mostro += self.nome[i].lower()
            else:
                nome_mostro += self.nome[i].upper()
        return f"Mostro: {nome_mostro}"

def pariUguali(a:list[int],b:list[int])->list:
    c:list=[]

    for i in range(len(a,b)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c

def combattimento(a:Alieno,m:Mostro)->None|str:

    if not isinstance(Alieno) or not isinstance(Mostro):
        return None
     
    munizioni_alieno=Alieno.getMunizioni
    assalto_mostro=Mostro.getAssalto

    sfida= pariUguali(munizioni_alieno,assalto_mostro)

    vincita=sfida.count(1)
    
    if vincita > 4:
        for i in range(3):
            print(m.getVittoria())
        return m
    else:
        print(m.getSconfitta)
        return a


def proclamaVincitore(c: Creatura):
    

