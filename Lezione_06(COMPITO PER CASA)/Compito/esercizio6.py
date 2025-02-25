n1=int(input("Inserisci primo numero: ")) 
n2=int(input("Inserisci secondo numero: ")) 
prodotto= 1                                         #inizializzo il prodotto a 1    
if n1<n2:                                       #Ciclo se n1 è min o = di n2,prodotto è
    while n1<=n2:                           #Ciclo da n1 a n2, inclusi
        prodotto *= n1                  #Moltiplico per 1
        n1 += 1                       #Sommo di 1 ad ogni iterazione
        
    print(f"Il prodotto è: {prodotto}")                 #Output
    
    
elif n1 > n2:
    while n2<=n1:
        prodotto *= n2
        n2 += 1
    print(f"Il prodotto che cercavi è: {prodotto}")
        


    

        




        
