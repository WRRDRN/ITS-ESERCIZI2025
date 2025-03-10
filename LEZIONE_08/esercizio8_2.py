'''Libro preferito: scrivi una funzione chiamata favorite_book() 
che accetti un parametro, titolo. La funzione dovrebbe stampare 
un messaggio, come "Uno dei miei libri preferiti è 
Alice nel paese delle meraviglie". Chiama la funzione, 
assicurandoti di includere 
un titolo di libro come argomento nella chiamata di funzione.'''

def favorite_book(title) -> str:
    print(f"Il mio libro preferito è {title}")

domanda=input(f"Qual è il tuo libro preferito?")



favorite_book("DIOMIO")

