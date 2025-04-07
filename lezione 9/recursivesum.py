def RecursiveSum(n:int) -> int:
    if n<0:
        print(f"Error")
        return 0
    elif n == 0:
        return 0
    
print(RecursiveSum(-5))
print(RecursiveSum(0))


def RecursiveSum(n:int) -> int:
    if n<0:
        print(f"Error")
        return 0
    elif n == 0:
        return 0
    # if n is positive, compute recursive sum
    else:
        return (n + RecursiveSum(n-1))   
    




print(RecursiveSum(5))