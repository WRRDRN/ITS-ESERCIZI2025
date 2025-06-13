def bin_search(lista, numero) -> None:
    
    mid: int = len(lista) // 2
    
    if lista[mid] == numero:
        
        print("Il numero è stato trovato!")
        #return None
        
    elif len(lista) == 1:
        
        print("Il numero non c'è!")
    
    elif lista[mid] > numero:
        
        bin_search(lista[:mid], numero)
        
    elif lista[mid] < numero:
        
        bin_search(lista[mid + 1:], numero)
        
    else:
        
        pass