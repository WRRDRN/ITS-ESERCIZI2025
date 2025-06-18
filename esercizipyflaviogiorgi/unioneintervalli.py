def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    # Ordina la lista degli intervalli in base all'inizio
    for i in range(len(intervals)):
        for x in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[x][0]:
                intervals[i], intervals[x] = intervals[x], intervals[i]

    merge = [intervals[0]]

    for i in range(1, len(intervals)):
        ultimo = merge[-1]
        corrente = intervals[i]

        if corrente[0] <= ultimo[1]:
            ultimo[1] = max(ultimo[1], corrente[1])
        else:
            merge.append(corrente)

    return merge

lista = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(lista))
