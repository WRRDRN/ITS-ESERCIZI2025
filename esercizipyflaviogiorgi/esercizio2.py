#Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
#classifichi i numeri in liste separate per numeri positivi e negativi.

def num(lista:list)-> dict:
    l_1:list=[]
    l_2:list=[]

    d_1:dict={}
    for num in lista:
        if num  >= 0:
            l_1.append(num)
        else:
            l_2.append(num)
    
    d_1={"positivi":l_1 , "negativi": l_2}
    return d_1



