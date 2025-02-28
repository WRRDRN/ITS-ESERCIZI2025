
listthree:int=[]

for i in range(3,31,3):
    listthree.append(i)

print(f"I primi 3 numeri sono: {listthree[:3]}")
print(f"I 3 centrali sono: {slice(3,6)}")