'''Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Create a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open. Create an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.

'''


class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        
        self.name= resturant_name
        self.type= cuisine_type
        
    def describe_resturant(self):
        print(self.name,self.type)


resturant1= Resturant("Nome","Tipo")
resturant1.describe_resturant()
resturant2= Resturant ("Nome2","Tipo2")
resturant2.describe_resturant()
resturant3= Resturant ("Nome3","Tipo3")
resturant3.describe_resturant()


        
