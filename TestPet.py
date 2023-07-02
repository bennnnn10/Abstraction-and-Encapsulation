import tkinter as tk
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

def display_information():
    pet_name = pet.get_name()
    animal_type = pet.get_animal_type()
    age = pet.get_age()

    information  = f"The name of your pet is {pet_name}\n"
    information += f"{pet_name} is a {animal_type}\n"
    information += f"Your pet {pet_name} is {age} year/s old."

     # Tkinter window
    window = tk.Tk()
    window.title("Vetcare")
    window.geometry("400x200")

    # Header Label
    header_label = tk.Label(window, text="Pet's Information", font=("Helvetica", 14, "bold"))
    header_label.pack(pady=10)

    # Label to display the information
    label = tk.Label(window, text=information, font=("Helvetica", 12))
    label.pack(pady=10)

    # Button to close the window
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack()

    window.mainloop()

display_information()