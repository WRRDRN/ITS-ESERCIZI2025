'''Scrivi una funzione chiamata make_shirt() che accetti una taglia e il testo di un messaggio 
che dovrebbe essere stampato sulla maglietta. La funzione dovrebbe stampare una frase che riassuma la taglia della maglietta e il messaggio stampato su di essa. 
Chiama la funzione una volta usando argomenti posizionali per creare una maglietta. 
Chiama la funzione una seconda volta usando argomenti per parole chiave.'''

def make_shirt(taglia, messaggio):
    print(f"The shirt size is {taglia} and it has the message: '{messaggio}'.")

#con i posizionali
make_shirt('M', 'dio!')

#Chiamata ad argomenti
make_shirt(taglia='L', messaggio='cane')
