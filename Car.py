#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

class Car:
    # Constructor
    def __init__(self, yearmodel, make):
        # Private Members
        self.__yearmodel = yearmodel
        self.__make = make
        self.__speed = 0 

    def accelerate(self):
        # Increases the car's speed by 5
        self.__speed += 5

        # Decreases the car's speed by 5