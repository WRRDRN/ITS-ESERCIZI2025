phrase= input("Inserisci una frase: ") #Creo input
i=len(phrase) -1 #Abbiamo accesso all'ultimo carattere della frase
for character in phrase: #Ciclo for per ogni carattere nella frase
     print(phrase[i],end='') #Output 
     i-= 1 #Indice che diminuisce di 1 fino alla fine della frase
   
