mylistA = [23,54,32,46,5] #lista 
mylistB = [7,84,59,10,11] #lista
mylistC = [] #listavuota
n=len(mylistA) #lunghezza della listaA

for i in range(n):
    totale = mylistA[i] + mylistB[- 1 - i]      #Ogni int nella A si somma all B partendo dall'ultimo indice
    mylistC.append(totale)                      #Aggiorno Lista c
    
print(f"ListaA: ",mylistA)
print(f"ListaB: ", mylistB)
print(f"Lista C: ", mylistC)
    
    