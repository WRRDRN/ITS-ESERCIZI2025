#Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
#restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50,
# ma
#con i prezzi aumentati del 10% e arrotondati a due cifre decimali.


def products(d1:dict)->dict:
    d_2:dict={}

    for k,v in d1.items():
        if v < 50:
            d_2.update((k, round(d1[k] + d1[k] * 0.10)))
        else:
            continue
    return d_2

    