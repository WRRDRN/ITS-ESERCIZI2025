'''LA SINTASSI PER DEFINIRE LA FUNZIONE E' 'DEF', SUPPIONIAMO DI 
DOVER SOMMARE I NUMERI DA 1 A 10.DA 20 A 37, E DA 35 A 49'''


'''SENZA LA FUNZIONE'''

'''sum:int= 0
for i in range(1,11):
    sum += i
print(f"La somma da 1 a 10 è: {sum}")'''

'''Per fare una funzione dobbiamo definirla (def),se io definisco la funzione ma
non la definisco è inuitle. COme si definisce: 
(key)def (spazio+nomedellafunzione+apro le parentesi) e poi due punti
RISCRIVIAMO L'ESERCIZIO DI PRIMA:

def sumInRange(a:int, b:int):
        result:int = 0
        for i in range(a, b+1):
                result = result + i
        return result

mysum = sumInRange(1, 10)
print(f”Sum from 1 to 10 is {sumInRange(1, 10)}”)
    
mysum= sum in range(1,10)
print(f"Somma da 1 a 10 è {SumInRange(1,19)}"'''

'''La funzione verrà chiamata SumInRange(al posto di functionName)
La funzione è un gruppo di statment per un'operazione:
realizzando una specifica operazione,assegno il nome alla funzione, che mi identifica
questo gruppo di istruzioni,ogni volta che devo esguire quella operazione, 
il la eseguo chuiamandola per nome.
Scrivi una funzione chiama subtract e calcoli la sottrazioni dei due numeri in input, il risuktato deve essere in output:
 '''

def subtract(a:int, b:int):
        result:int = a - b
        return result
myresult = subtract(4, 1)

print(myresult)   #SSENZA INPUT

#-------------------------------PORCODIO------------------------#

def subtract(a:int, b:int):
    result= a - b
    return result


a=int(input('Inserisci un numero:' ))
b=int(input('Insersci un numero:'))


print(f"{a} meno {b} fa {subtract(a,b)}") #CON INPUT