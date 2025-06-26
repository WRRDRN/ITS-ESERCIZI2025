import random

def genera(dim:[int])->list[list[int]]:
    mat:list=[]
    for c in range(dim):
        row=[]
        for c in range(dim):
            while True:
                X= random.randint(0,13)
                if c==0:
                    row.append(X)
                    break
                if x != row[0]:
                    row.append(X)
                    break
    mat.append(row)

