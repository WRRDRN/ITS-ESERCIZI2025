from string import ascii_lowercase, ascii_uppercase

s: str = "ciao"

def cifrario(s: str, chiave: int) -> str:
    
    risultato: str = ""
    
    for carattere in s:
        
        
        if carattere in ascii_lowercase:
            index: int = ascii_lowercase.index(carattere)
            
            index = (index + chiave) % len(ascii_lowercase)
            
            risultato += ascii_lowercase[index]
            
        elif carattere in ascii_uppercase:
            index: int = ascii_uppercase.index(carattere)
            
            index = (index + chiave) % len(ascii_uppercase)
            
            risultato += ascii_uppercase[index]     
            
        else:
            
            risultato += carattere
               
    return risultato
