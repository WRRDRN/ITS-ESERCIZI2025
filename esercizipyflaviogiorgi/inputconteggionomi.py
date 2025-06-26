nomi = []
max_nomi = 30

while len(nomi) < max_nomi:
    nome = input("Inserisci un nome: ").strip()

    if nome == "":
        print("Il nome non esiste.")
        continue
    if len(nome) >= 20:
        print("Il nome deve avere meno di 20 caratteri.")
        continue
    if nome in nomi:
        print("Nome è già inserito")
        break

    nomi.append(nome)

print(f"Totale nomi inseriti: {len(nomi)}")

if nomi:
    nomelunghissimo = max(nomi, key=len)
    print(f"Nome lunghissimo: {nomelunghissimo}")
    print(f"Lunghezza caratteri nome lunghissimo: {len(nomelunghissimo)}")
else:
    print("Nessun nome valido è stato inserito.")

    


        


