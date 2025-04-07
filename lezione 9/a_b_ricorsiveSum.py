def sumInRange(a:int, b:int) -> int:
# if a > b, swap values of a and b
    if a > b:
# define a temporary variable called temp, containing value of a
        temp:int = a
# swap values of a and b
        a = b
        b = temp # now b = a
# define a sum
    sum:int = 0
# compute sum until b = a
    while b>=a:
        sum = sum + b
        b = b -1
# return sum
        return int(sum)

print(sumInRange(5,10))
