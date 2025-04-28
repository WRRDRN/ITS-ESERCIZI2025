class Person:
    def __init__(self, cf, name, surname, age):
        self._cf = cf
        self._name = name
        self._surname = surname
        self._age = age

    def get_cf(self):
        return self._cf
    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self._age


class Student(Person):
     def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self._group = None

        def set_group(self, group):
            self._group = group
        def get_group(self):
            return self._group


class Lecturer(Person):
    pass

class Group:
    def __init__(self,name):
        self.name= name
        self.groups= []
        
    def groups(self):
        return self.groups
        
    def add_group(self, group):
        self.groups.append(group)

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                return
                print("Diocan")
        
