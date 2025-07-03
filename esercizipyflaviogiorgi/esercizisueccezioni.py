import math
"Radice quadrata sicura: scrivi una funzione safe_sqrt(numero) "
"che calcoli la radice quadrata di un numero utilizzando math.sqrt(). "
"Gestisci ValueError se l'input è negativo restituendo un messaggio informativo."

def safe_sqrt(numero:int):
    try:
        return math.sqrt(numero)
    except:
        return ValueError 
       
print(safe_sqrt(-43))
  


