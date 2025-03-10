def makealbum(artist:str,album:str,label:None):
    album:dict={"artist":artist,"album":album,"label":label}
    return(album)

print(makealbum("Dio","Cane","34"))
print(makealbum("fischio","fesa","45,3"))
print(makealbum("codio","fes","fus"))



