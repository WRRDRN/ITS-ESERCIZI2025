lista_numeri=[] #Creazione lista vuota per l'append del ciclo if\elif
somma_interi_inseriti= 0 #Inizializzo a 0 i numeri inseriti
totale_numeri_interi= 0 #Inizializzo a 0 il totale dei numeri interi inseriti

while True:
    numero=float(input("Inserisci numero: ")) #Converto input in float
    if numero < 0:
        break                                 #Fermo il ciclo se viene inserito un negativo

    elif numero.is_integer():
        somma_interi_inseriti += numero     #Aggiorna somma totale interi
        totale_numeri_interi += 1           #Totale n. interi inseriti
        lista_numeri.append(numero)         #Aggiorna lista
    
    else:  
        lista_numeri.append(numero)         #Aggiorna lista
        
media_numeri_interi = somma_interi_inseriti / totale_numeri_interi
numeromax=max(lista_numeri)
numeromin=min(lista_numeri)

print(f"Il numero più grande inserito è {numeromax}") #Serie di Output
      
print(f"Il numero più piccolo inserito è {numeromin}")

print(f"La media dei tuoi numeri interi è: {media_numeri_interi}")

            
        
        
        
        