while True:
    parola=(input("Inserisci una parola:")).lower()  #Creo l'input e con il .lower faccio si che in output sia tutto minuscolo
    if parola == "fine":
        break                                        #Sviluppo il break dopo la parola 'fine'
    if parola[0]==parola[-1]:
        print(f"La parola '{parola}' ha la lettera iniziale corrispondente a quella finale!!") #Output
    else:
        print(f"la parola '{parola}' ha la lettera iniziale diversa da quella finale!!") #Output
