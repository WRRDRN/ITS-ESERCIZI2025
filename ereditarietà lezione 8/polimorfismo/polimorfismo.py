from persona import Persona
from alieno import Alieno

'''creare un oggetto p per la classe Persona'''
p: Persona= Persona("Adriano","Morra",28)

'''visualizziamo del info della persona P'''
print(p)

'''creare un oggetto 'ET' della classe Alieno'''

et: Alieno=Alieno("Andromeda")
print(et)

et.speak()
