#Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
#soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
#è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
#oppure "Azione negata" a seconda delle condizioni che sono soddisfatte

def combo(x:bool,y:bool,z:bool)-> str:
    if x and (y or z) :
        print("Azione permessa")
    else:
        print("Azione negata")

print(combo(False,False,False))

