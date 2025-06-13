'''Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze'''
'''text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}'''

from string import punctuation

def count_unique_words(text:str)-> dict[str,int]:

    words_freq:dict[str,int]={}

    text:str=text.lower()

    text_list:list[str]=text.split(" ")

    for token in text_list:
        clean_text_list: str = token.strip(punctuation)
        if clean_text_list in words_freq:
            words_freq[clean_text_list]+=1
        
        else:
            words_freq[clean_text_list]=1

    return words_freq