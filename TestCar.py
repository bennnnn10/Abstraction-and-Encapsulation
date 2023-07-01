import pyfiglet
from termcolor import colored

from Car import Car

#Greetings
print(pyfiglet.figlet_format("Welcome".center(11), justify="center", font="speed"))
print("\n")

model = "\033[;33;1;3mHonda Civic Type R\033[0m"
print("\033[;33;1;3m                   This\033[0m", model, "\033[;33;1;3mis starting...\033[0m")
print("\033[;33;1;3mPlease press enter\033[0m".center(90))
print(input("".center(38)))

# Car Information
car_info = Car(2022, "Honda Civic Type R")

# Accelerates 5 times
print()
print("-" * 78)
print("\033[;31;1;3mAccelerating\033[0m".center(90))
print("-" * 78)
print("\n")

for _ in range (1):
    car_info.accelerate()
    speed = car_info.get_speed()
    print("The car's speed right now is", speed)

for _ in range (1):
    car_info.accelerate()
    speed = car_info.get_speed()
    print("Accelerating to", speed)

for _ in range (1):
    car_info.accelerate()
    speed = car_info.get_speed()
    print("Accelerating to", speed)

for _ in range (1):
    car_info.accelerate()
    speed = car_info.get_speed()
    print("Accelerating to", speed)

for _ in range (1):
    car_info.accelerate()
    speed = car_info.get_speed()
    print("The current speed is", speed)

input("".center(38))

# Brakes 5 times
print()
print("-" * 78)
print("\033[;31;1;3mDecelerating\033[0m".center(90))
print("-" * 78)
print("\n")

for _ in range (1):
    car_info.brake()
    speed = car_info.get_speed()
    print("The current speed is", speed)

for _ in range (1):
    car_info.brake()
    speed = car_info.get_speed()
    print("Decelerating to", speed)

for _ in range (1):
    car_info.brake()
    speed = car_info.get_speed()
    print("Decelerating to", speed)

for _ in range (1):
    car_info.brake()
    speed = car_info.get_speed()
    print("Decelerating to", speed)

for _ in range (1):
    car_info.brake()
    speed = car_info.get_speed()
    print("The car's speed right now is", speed)

print("\n")
print("-" * 78)
print()
print("\033[;31;1;3mTurning off the engine...\033[0m".center(90))
print()

print("\n")
print("✧" * 78)
print()
print(pyfiglet.figlet_format("Honda Civic".center(11), justify="center", font="speed"))
print("✧" * 78)
print("\n")