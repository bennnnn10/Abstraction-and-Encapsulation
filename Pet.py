#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

class Pet:
    # Constructor
    def __init__(self):
        # Private Members
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Setter Method
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.age = age
        
    # Getter Method
    def get_name(self):
        # Getting the name
        return self.__name
    
    def get_animal_type(self):
        # Getting animal type
        return self.__animal_type
    
    def get_age(self):
        #Getting its age
        return self.__age