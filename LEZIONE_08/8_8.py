def makealbum(artist:str,album:str):
    album:dict={"artist":artist,"album":album}
    return(album)


while True:

    risparti=input("Inserisci arista preferito: ")
    if risparti == 'quit':
        break
    rispalbum=input("Inserisci album: ")
    if rispalbum == 'quit':
        break

    albumdic=makealbum(risparti,rispalbum)
    print(f"Il tuo artista e il tuo album preferito è: {albumdic['artist']}{albumdic['album']}")

    