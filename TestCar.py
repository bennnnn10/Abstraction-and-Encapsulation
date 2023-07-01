from Car import Car

# Car Information
car_info = Car(2022, "Honda Civic Type R")

# Accelerates 5 times
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

# Brakes 5 times