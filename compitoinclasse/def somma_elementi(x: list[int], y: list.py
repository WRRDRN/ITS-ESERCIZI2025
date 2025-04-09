def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    newlist:list= []
    for i in range(len(x)):
        result = x[i] + y[i]
        newlist.append(result)
    return newlist

