from Pet import Pet

pet = Pet()

pet_name = input("What is the name of your pet? ")
animal_type = input("What type of animal is your pet? ")
age = int(input("How old is you pet? "))

pet.set_name(pet_name)
pet.set_animal_type(animal_type)
pet.set_age(age)

print("The name of your pet is", pet.get_name())
print(pet.get_name(), "is a", pet.get_animal_type())
print("Your pet", pet.get_name(), "is", pet.get_age(), "year/s old.")