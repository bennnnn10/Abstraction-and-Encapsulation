from Fan import Fan

fan_1 = Fan()
fan_1.set_speed(Fan.FAST)
fan_1.set_radius(10)
fan_1.set_color("yellow")
fan_1.set_on(True)

# For fan #1 output
print("Fan #1 Status")
print("The current speed of fan #1 is", fan_1.get_speed())
print("Its radius is", fan_1.get_radius())
print("And the color is", fan_1.get_color())
print("On:", fan_1.get_on())

fan_2 = Fan()
fan_2.set_speed(Fan.MEDIUM)
fan_2.set_radius(5)
fan_2.set_color("blue")
fan_2.set_on(False)

#For fan #2 output
print("Fan #2 Status")
print("The current speed of fan #2 is", fan_2.get_speed())
print("Its radius is", fan_2.get_radius())
print("And the color is", fan_2.get_color())
print("On:", fan_2.get_on())