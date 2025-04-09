class User:


    def __init__(self,firstname,lastsurname,age,email):
        self.name=firstname
        self.surname=lastsurname 
        self.age= age
        self.email=email

    def desribeuser(self):
        print(f"Name= {self.name}")
        print(f"Surname: {self.surname}")
        print (f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Ciao {self.name}!")


user1 = User("Giovanni","Sacco",23,"giovanni@gmail.com")
user2 = User("Antonia","Dessi",33,"dessi@gmail.com")
user3= User("Roberto","Contono",43,"contonobomber@gmail.com")

print("User 1=")
user1.desribeuser()
user1.greet_user()

print("User2=")