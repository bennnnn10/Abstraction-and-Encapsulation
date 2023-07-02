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