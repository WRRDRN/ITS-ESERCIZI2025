euro_disponibili = int(input("Insersci denaro:")) #Input
barretta_acquistabili = 0 #Inizializzo variabile delle barrette acquistabili in base all'Input
buono_sconto = 0 #Creo variabile per trovare il buono sconto alla sesta barretta


while euro_disponibili > 0: #Ciclo per definire i pezzi acquistati, la sottrazione degli euro e la somma del buono sconto
    barretta_acquistabili += 1
    euro_disponibili -= 1
    buono_sconto += 1
    
    if buono_sconto == 6: #Ciclo per definire che se i buoni sconti sono 6->buono sconto +1
            barretta_acquistabili += 1 #barretta'gratuiuta'
            buono_sconto -= 6 #Ad ogni 6 buono sconto, azzero

else:
    print(f"Hai acquistato {barretta_acquistabili} barretta/e.")
    print(f"Hai {buono_sconto} buoni sconto.")