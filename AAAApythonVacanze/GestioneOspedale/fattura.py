from gestioneOspedale import Persona
from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self,patient,doctor):
        self.patient=patient
        self.doctor=doctor
    
        if self.doctor.isAValidDoctor():
            self.fatture=len(self.patient)
            self.salary=self.doctor * self.fatture
        else:
            self.patient= None
            self.doctor=None
            self.parcel=None
            self.salary=None
            print("Il dottore non è valido")

    def getSalary(self):
        if self.doctor is not None and self.patient is not None:
            self.salary=self.doctor * len(self.patient)
            return self. salary
        return 0
         
    def getFatture(self):
        if self.patient is not None:
            self.fatture= len(self.patient)
            return self.fatture
        return 0    
    
    def addPatient(self,newPatient):
        if self.patient is not None:
            self.patient.append(newPatient)
            self.getFatture
            self.getSalary
            print (f'Alla lista del {self.doctor.last_name} è stato aggiunto il paziente {self.idCode}')


        
    def rmPatient(self,idCode):
        if self.patient is None:
            print('Impossibile rimuovere il paziente')
        
        patientrm=None
        for patient in self.patient:
            if patient.getidCode() == idCode:
                patientrm=patient
                break
        if patientrm:
            self.patient.remove(patientrm)
            self.getFatture()
            self.getSalary()
            print(f"Del Dottor {self.doctor.last_name} è stato rimosso")
        else:
            print(f"Paziente {idCode} non trovato")

