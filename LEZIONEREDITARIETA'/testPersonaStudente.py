from persona import Persona
from studente import Studente

#creare un oggetto p di classe Persona
p: Persona= Persona("Adriano","Morra",29)

#visualizzare le informazioni relative alla persona p 
print(p)

#creare un oggetto della classe Studente

studente: Studente = Studente('Mario','Rossi',53,"432314")
#CONTROLLO SE STUDENTE UNO SIA ISTANZA DELLA CLASSE STUDENTE CON 'ISISTANCE'
if isinstance(studente,Studente):
    print (f"\nStudente è un oggetto di Studente")

#voglio sapere se studente sia anche istanza di Persona, dato che la classe studente eredità dalla classe Persona

if isinstance (studente, Persona):
    print(f"L'oggetto Studente è anche istanza della classe Persona")
else:
    print(f"E'solo della classe Studente..")

#Voglio controllare che l'oggetto p sia istanza di Persona
if isinstance(p,Persona):
    print(f"p E'istanza è Persona")

if isinstance (p,Studente):
    print(f"L'oggetto p è istanza della classe Persona ed è anche istanza dela classe studente")
else:
    print(f"Non lo è")
    #VOGLIO CONTROLLARE SE STUDENT E' SOTTOCLASSE DELLA CLASSE PERSONA
    #con la funzione ISSUBCLASSE CON DUE PARAMETRI (CLASS1,CLASS2), CHE CONTROLLA SE CLASS1(STUDENTE) E' SOTTO CLASSE DI CLASS2(PERSONA)

if issubclass(Studente,Persona):
    print(f"Studente è sottoclasse di Persona")

print(studente)
print(p)

print(f"\nLa media dei voti relativi agli esami sostenuti dallo studente è: {studente.getMediaEsame([10,20,30])}")

#creiamo studente2 della classe studente

studente2:Studente=Studente(p.getName(),p.getSurname(),p.getAge(),"4930220")

print(f"\n", studente == p)
print(f"\n",studente == studente2)

#verifichiamo se è uguale a se stesso
print(f"\n",studente == studente)

#modificare nome, cognome, età dello studente2 affinchè abbia stesso nome, cognome e stessa età dellom studente

studente2.setName(studente.getName())
studente2.setSurname(studente.getSurname())
studente2.setAge(studente.getAge())

print("\n",studente == studente2)


#forzo la matricoladello studente2 con qiella dello studente1
studente2.setMatricola(studente.getMatricola())

#confronto se studente è uguale a studente 2
print("\n",studente == studente2)

