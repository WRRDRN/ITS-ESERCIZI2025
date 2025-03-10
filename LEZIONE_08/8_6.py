'''Scrivi una funzione chiamata city_country() che prenda il nome di una città e del suo paese. 
La funzione dovrebbe restituire una stringa formattata in questo modo: "Santiago, Cile". 
Chiama la tua funzione con almeno tre coppie città-paese e stampa i valori restituiti.
'''

def city_country(città='Bari',paese='Nova Yocchi'):
    print(f"{città},{paese}")

city_country('Buenos Aires','Argentina')
city_country('Havana','Cuba')
city_country('Amsterdam','Olanda')