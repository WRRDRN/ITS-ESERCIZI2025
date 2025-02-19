defunto:list[str]=["Berlusconi","Gheddafi","Paul McCartney"]
for item in defunto:
    print(f"Ehi,{item}, andiamo a mangiare sushi?")

defunto[0]="Giuseppe"
print(defunto)
for item in defunto:
    print(f"Ehi,{item}, andiamo a mangiare sushi?")