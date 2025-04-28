from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):
    def __init__ (self):
        super().__init__()
        self.setShape("rettango")


    def draw(self) -> None:
        print(f"\n{self.getShape}\n")

        #outer for

    for i in range(5):
        #inner for
        for j in range(5*2):

            #lato a lato b rettangolo
            if i == 0 or i == 5-1:
                print(f"*",end="")

        #lato b e lato c
            elif j== 0 or j==5*2 -1:
                print("*",end=" ")
            else: #per la spaziatura
                print(" ",end=" ") 
        print("\n", end=" ")
                

    
            
