# Scrivi una funzione che moltiplica tutti i numeri interi di una lista 
# che sono minori di un dato valore intero definito threshold.

numeri:list=[4,1,5,6,7,83,20,12,67,14,16,18,25,28]



def lista(x:list,threshold:int)-> list:

    product = 1 

    if x:

        for num in x:


            if num <=threshold:

                product *= num

    else:

        product = 0

    return product



print(lista(numeri, ))

    

    
            
        
