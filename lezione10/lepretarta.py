

import random

def stampa_posizione(pos_tartaruga, pos_lepre):
    corsa = ['_'] * 70
    if pos_tartaruga == pos_lepre:
        corsa[pos_tartaruga - 1] = 'OUCH!!!'
    else:
        corsa[pos_tartaruga - 1] = 'T'
        corsa[pos_lepre - 1] = 'H'
    print(' '.join(corsa))

def muovi(pos, tipo):
    mossa = random.randint(1, 10)
    if tipo == 'tartaruga':
        if 1 <= mossa <= 5: return 3  # Passo veloce
        if 6 <= mossa <= 7: return -6  # Scivolata
        return 1  # Passo lento
    if tipo == 'lepre':
        if 1 <= mossa <= 2: return 9  # Grande balzo
        if 3 <= mossa <= 4: return -12  # Grande scivolata
        if 5 <= mossa <= 7: return 1  # Piccolo balzo
        if 8 <= mossa <= 9: return -2  # Piccola scivolata
        return 0  # Riposo

def gara():
    pos_tartaruga, pos_lepre = 1, 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while pos_tartaruga < 70 and pos_lepre < 70:
        pos_tartaruga += muovi(pos_tartaruga, 'tartaruga')
        pos_lepre += muovi(pos_lepre, 'lepre')

        # Evita che gli animali vadano sotto il quadrato 1
        pos_tartaruga = max(1, pos_tartaruga)
        pos_lepre = max(1, pos_lepre)

        stampa_posizione(pos_tartaruga, pos_lepre)

        # Verifica se uno dei due ha vinto
        if pos_tartaruga >= 70 and pos_lepre >= 70:
            print("IT'S A TIE.")
            break
        elif pos_tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif pos_lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break

# Avvia la gara
gara()
