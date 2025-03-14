
#DA RICONTROLLARE
class User:

    def __init__(self,first_name,last_name,greet):

        self.first_name= first_name
        self.last_name=last_name
        self.greet = greet

    def describe_user(self):
        print(self.first_name,self.last_name)


    def greet_user(self):
        print(self.greet)



       

Greet = User("Nome", "Cognome", "Ciao Utente")
Greet.greet_user()  
Greet.describe_user()

User1= User ("Nome","Cognome","Ciao Utente")
User1.describe_user()


User2= User ("Nome", "Cognome","Ciao Utente2")
User2.describe_user()


User3= User("Nome", "Cognome","Ciao Utente 3")
User3.describe_user()

