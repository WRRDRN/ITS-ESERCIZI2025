# dal file persona.py importa la classe Persona
from persona import Persona

#creo una persona
admo:Persona = Persona("Adriano","Morra",28)

print(admo)

print(admo.name,admo.lastname,admo.age)

#richiamare la funzione displayData

admo.displayData()

print("----------------------------------------------------")

#dal file persona2 importa la classe Persona

from persona2 import Persona

admo:Persona = Persona()

#richianmo la funzione displaydata della classe perosna per mostrare in output le info relative all'oggetto admo

admo.displayData()

#MODIFICARE IL NOME DELLA PERSONA ADMO

admo.setName("Adriano")

print("-------------")

admo.displayData()

#MODIFICARE IL NOME DELLA PERSONA ADMO

admo.setLastName("Morra")

print("------------")

admo.displayData()

#MODIFICARE IL NOME DELLA PERSONA ADMO

admo.setAge(28)


admo.displayData()


print("°°°°°°°°°°°°°°°°")

print(admo.getName(), admo.getLastName(), admo.getAge())