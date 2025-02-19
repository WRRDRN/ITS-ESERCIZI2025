# insert a number
n:int = int(input("Insert finishing Position: "))
# match statement
match n:
# n=1
    case 1:
        print(f"{n}st!")
# n=2
    case 2:
        print(f"{n}nd!")
# n=3
    case 3:
        print(f"{n}rd!")
# default case
    case _:
        print(f"{n}th!")
