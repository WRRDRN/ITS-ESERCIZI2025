def valore_mano(carte):
    totale = 0
    assi = 0
    
    # Sommiamo il valore delle carte
    for carta in carte:
        match carta:
            case 11:  # L'asso
                totale += 11
                assi += 1
            case valore if 2 <= valore <= 10:  # Le carte numeriche
                totale += valore
    
    # Se la somma supera 21, riduciamo gli assi da 11 a 1
    while totale > 21 and assi > 0:
        totale -= 10  # Riduciamo un asso da 11 a 1
        assi -= 1
    
    return totale
