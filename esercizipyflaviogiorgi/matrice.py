'''Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1) sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2) sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).
Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15'''


m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def diag(m: list[list[int]])->int:

    somma:int=0
    somma_2:int=0

    for i in range(len(m)):
        somma += m[i][i]
        somma_2 += m[i][len(m)- 1- i]