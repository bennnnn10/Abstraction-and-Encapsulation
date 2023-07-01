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