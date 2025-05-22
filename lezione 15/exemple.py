def bubblesort(lista: list[int]):

    orderer:bool= True
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):

            if lista[i]>=lista[j]:

                orderer=False

            
    if orderer:
        return lista



lista:list = [6,3,5,76,5,98,12]
ordinato=bubblesort(lista)
print(ordinato)