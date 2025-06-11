class ContactManager:

    def __init__(self):
        self.contacts:dict[str,list[str]]={}


    def create_contact(self,name:str,phone_num:list[str])-> dict|str:
        if name in self.contacts:
            return "Errore, il contatto c'è già"
        else:
            self.contacts[name]=phone_num
        return{name:phone_num}
    
    
    def add_phone_number(self,contact_name:str,phone_number:str)->dict:
        if contact_name not in self.contacts:
            return (f"Il contatto non esiste")
        if phone_number in self.contacts[contact_name]:
            return(f"Il contatto esiste già")
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}