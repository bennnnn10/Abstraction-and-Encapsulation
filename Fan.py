#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

class Fan:
    # Three constants named SLOW, MEDIUM, and FAST with the values 1,2, and 3.
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor
    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        # Private Methods
        # Private int data field named speed
        self.__speed = int(speed)
        # Private bool data field named on that specifies whether the fan is on
        self.__on = bool(on)
        # Private float data field named radius
        self.__radius = float(radius)
        # Private string data field named color
        self.__color = str(color)

    # Getter Method
    def get_speed(self):
        # Speed
        return self.__speed
    
    def get_on(self):
        # On/Off
        return self.__on
    
    def get_radius(self):
        # Radius
        return self.__radius
    
    def get_color(self):
        # Color
        return self.__color
    
    # Setter Method
    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_on(self, on):
        self.__on = bool(on)

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)