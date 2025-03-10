'''Magliette grandi: modifica la funzione make_shirt() in modo che le magliette siano grandi di default con un messaggio che recita I love Python. 
Crea una maglietta grande e una maglietta media con il messaggio di default e una maglietta di qualsiasi taglia con un messaggio diverso.'''

def make_tshirt (size='XL', messagge='Ilovedio'):
    print(f"La taglia è {size} e il messaggio è {messagge}")


result= make_tshirt()
result= make_tshirt('M')
result= make_tshirt('S','diocane')



