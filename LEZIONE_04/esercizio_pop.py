defunto:list[str]=["Berlusconi","Gheddafi","Paul McCartney"]
for item in defunto:
    print(f"Ehi,{item}, andiamo a mangiare sushi?")

defunto[0]="Giuseppe"



for item in defunto:
    print(f"Ehi,{item}, andiamo a mangiare sushi?")



defunto.insert(0,"Mao")
defunto.insert(3,"Francisco Franco")
defunto.insert(5,"Gianni Alemanno")



for item in defunto:
    print(f"Ehi,{item}, andiamo a mangiare sushi?")



defunto.pop(0)
print(f"Mi dispiace Giusè, è successo un macello, niente più cena")
defunto.pop(1)
print(f"Mi dispiace Gheddà, è successo un macello, cena annullata")
defunto.pop(2)
print(f"Paul, niente, cena annullata")
for item in defunto:
    print(f"{item},sei ancora invitato!")
