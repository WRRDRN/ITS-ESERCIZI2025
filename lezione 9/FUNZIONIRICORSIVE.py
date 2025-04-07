def recursive_Countdown (n:int) -> None:
    if n < 0: # prima scrivo la condizione d'errore
        print(f"Error")
    elif n == 0:
        print(f"0")
    else:
        print(n)
        recursive_Countdown(n-1)    #inserisco l'operazione da fare


recursive_Countdown(5) #richiamo la funzione countdown dando il valore 5


def countdown(n:int) -> None: #OMETTERE L'ELIF
    # n is negative
    if n < 0 :
        print("Error! Inserted number is negative!")
    # other cases
    else:
        print(n)
        countdown(n-1)

recursive_Countdown(5)

