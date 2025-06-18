def calculateCharges(car: str, ora: float) -> str:
    totale = 0.0
    
    if ora <= 3:
        totale = 2.00
    elif ora < 24:
        ore_extra = ora - 3
        totale = 2.00 + (ore_extra * 0.50)

    elif ora == 24:
        totale = 10.00

    else:
        return f"{car} {ora} "
    
    return f"{car} {ora} {totale:.2f}"


car1 = calculateCharges("car1", 1.5)
car2 = calculateCharges("car2", 4.0)
car3 = calculateCharges("car3", 24.0)



print(car1)
print(car2)
print(car3)


     

