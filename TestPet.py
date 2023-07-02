from termcolor import colored
import pyfiglet

from Pet import Pet

print("\n")
print(colored("(\__/)".center(80), "yellow"))
print(colored("(='.'=)".center(80), "yellow"))
print(colored("('')_('')".center(80), "yellow"))

print("\n")
print("⍨" * 78)
print(pyfiglet.figlet_format("Vetcare".center(11), justify="center", font="bulbhead"))
print("⍨" * 78)
print("\n")

pet = Pet()

print("\033[;34;1;3mPet's Information Desk\033[0m".center(91))
print("\n")

print()
pet_name = input("\033[;1;3mWhat is the name of your pet? \033[0m")
print()
animal_type = input("\033[;1;3mWhat type of animal is your pet? \033[0m")

while True:
    try:
        print()
        age = int(input("\033[;1;3mHow old is your pet? \033[0m"))
        print("\n")
        print("⍨" * 78)
        break
    except ValueError:
        print()
        print("\033[;31;1;3mInvalid data. Please provide a valid age.\033[0m".center(91))

pet.set_name(pet_name)
pet.set_animal_type(animal_type)
pet.set_age(age)

print("The name of your pet is", pet.get_name())
print(pet.get_name(), "is a", pet.get_animal_type())
print("Your pet", pet.get_name(), "is", pet.get_age(), "year/s old.")