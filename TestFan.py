import pyfiglet
from termcolor import colored

from Fan import Fan

print("\n")
print("\033[;32;1;3m")
print("⍨" * 78)
print(pyfiglet.figlet_format("Electricfan".center(11), justify="center", font="speed"))
print("⍨" * 78)
print("\033[0m")
print("\n")

fan_1 = Fan()
fan_1.set_speed(Fan.FAST)
fan_1.set_radius(10)
fan_1.set_color("\033[;33;1;3myellow\033[0m")
fan_1.set_on(True)

# For fan #1 output
print(colored("\033[40mFan #1 Status\033[0m", "yellow"))
print("\n")
print("\033[;1;3mThe current speed of fan #1 is", fan_1.get_speed())
print("\033[;1;3mIts radius is", fan_1.get_radius())
print("\033[;33;1;3mAnd the color is\033[0m", fan_1.get_color())
print("\033[;1;3mOn:", fan_1.get_on())
print("\033[0m")
print("\n")
print("⍨" * 78)
print("\n")

fan_2 = Fan()
fan_2.set_speed(Fan.MEDIUM)
fan_2.set_radius(5)
fan_2.set_color("\033[;34;1;3mblue\033[0m")
fan_2.set_on(False)

#For fan #2 output
print(colored("\033[40mFan #2 Status\033[0m", "blue"))
print("\n")
print("\033[;1;3mThe current speed of fan #2 is", fan_2.get_speed())
print("\033[;1;3mIts radius is", fan_2.get_radius())
print("\033[;34;1;3mAnd the color is\033[0m", fan_2.get_color())
print("\033[;1;3mOn:", fan_2.get_on())

print("\033[;32;1;3m")
print("⍨" * 78)
print(pyfiglet.figlet_format("Thank You".center(11), justify="center", font="speed"))
print("⍨" * 78)
print("\033[0m")
print("\n")