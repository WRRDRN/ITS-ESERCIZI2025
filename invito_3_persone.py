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
