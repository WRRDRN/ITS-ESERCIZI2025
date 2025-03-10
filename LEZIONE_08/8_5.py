'''Scrivi una funzione chiamata describe_city() che accetti il ​​nome di una città e il suo paese. 
La funzione dovrebbe stampare una frase semplice, come Reykjavik è in Islanda. 
Assegna un valore predefinito al parametro per il paese. 
Chiama la tua funzione per tre città diverse, 
almeno una delle quali non si trovi nel paese predefinito.'''

def describecity(città='Roma',paese='Italia'):
    print(f"Bella {città} che sta in {paese}")
    

describecity()
describecity('Milano')
describecity('Frosinone')
describecity('New York','America')