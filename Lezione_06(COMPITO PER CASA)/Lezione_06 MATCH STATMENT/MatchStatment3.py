
voto:int = int(input("Inserisci un voto: "))


match voto:
    case voto if voto in range(1,4):
        print(f"Gravemente insufficente!")
    case 4|5:
        print(f"Insufficente!")
    case 6|7:
        print(f"Sufficente!")
    case 8|9:
        print(f"Molto buono!")
    case 10:
        print(f"Eccellente!")
    case _:
        print(f"Voto non valido!")