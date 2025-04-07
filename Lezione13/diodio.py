class Resturant:

    def __init__(self,name,cuisine):
        self.name= name
        self.cuisine= cuisine

    def describe_resturant(self):
        print (f"Resturant name: {self.name}")
        print (f"Cuisine Type: {self.cuisine}")

    def openresturant(self):
        print(f"{self.name} è aperto!!!")


resturant=Resturant("E' Perfetto per me!","Colombian")

if __name__ == "__main__": 

    print(resturant.name)
    print(resturant.cuisine)

    resturant.describe_resturant()
    resturant.openresturant()


