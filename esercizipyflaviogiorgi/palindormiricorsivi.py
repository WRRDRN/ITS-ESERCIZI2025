def pal(words:str) -> bool:
    words = words.replace(" ","").lower()

    if len(words) <= 1:
        return True

    if words[0] != words[-1]:
        return False

    return pal(words[1:-1])


#print(pal("radar"))
#print(pal("Anna"))                     
#print(pal(" I topi non avevano nipoti"))
#print(pal("casa"))                         
#print(pal("Marta"))                
#print(pal("Roma e Amore"))   
# 
# 
