'''Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) 
nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, 
secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0'''

voto_input:str= input("Inserire voto di laurea:") #INPUT E' UNA STR NON UN INT


if voto_input.isnumeric(): #SE IL VOTO E' UN NUMERO->
    voto:int  = int(voto_input) #TRASFORMO IL VOTO IN INT

    match voto:
        case voto if voto in range(106,111):
            print(f"GPA 4.0")
        case voto if voto in range(101,106):
            print(f"GPA 3.7")
        case voto if voto in range(96,101):
            print(f"GPA 3.3")
        case voto if voto in range(91,96):
            print(f"GPA 3.0")
        case voto if voto in range(86,91):
            print(f"GPA 2.7")
        case voto if voto in range(81,86):
            print(f"GPA 2.3")
        case voto if voto in range(76,81):
            print(f"GPA 2.0")
        case voto if voto in range(70,76):
            print(f"GPA 1.7")
        case voto if voto in range(66,70):
            print(f"GPA 1,0")
        case _:
            print(f"Voto non valido")
else:
    print("Il voto non è un numero")
              
 