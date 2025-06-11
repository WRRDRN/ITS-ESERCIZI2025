#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, somma il valore al valore già associato alla chiave.


#tupla è immu=[(0,"val1"),(2,"val3")]
def covert_dict(lista:list[tuple])-> dict:
    dictionario_1:dict= {} #dichiara il dizionario
    for tupla in lista:#cerca le tuple nella lista
        key,value=tupla[0],tupla[1] #key fa rifrimento a 0 e value fa riferimento a 1
        if key in dictionario_1: 
            dictionario_1[key] += value
        else:
            dictionario_1[key]=value
    return dictionario_1  

