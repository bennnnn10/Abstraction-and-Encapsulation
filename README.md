# Abstraction and Encapsulation

The Python programming language is used to illustrate the ideas of abstraction and encapsulation in this program. Additionally, it has three (3) distinct classes: Fan, Car, and Pet. These three (3) classes each have distinct functions to be tackled below.

## Usage

### Fan Class
This code creates a fan class representing an electric fan. It includes methods for retrieving and configuring various fan parameters such as speed, status, radius, and color.


- `SLOW` with a value of 1, this parameter represents the fan's slow speed.
- `MEDIUM` with a value of 2, this parameter represents the fan's medium speed.
- `FAST`  with a value of 3, this parameter represents the fan's fast speed.
- `speed` (default: SLOW): Sets the fan's initial speed.
- `on` (default: False): Defines if the fan is switched on (True) or off (False) upon startup.
- `radius` (default: 5): Defines the fan's radius.
- `color` (default: "blue"): Identifies the fan's color.



### Car Class

This class replicates a car; it's similar to a real car in that you can brake and accelerate, change the speed, and control it; it also displays your current speed. Additionally, it enables users to interact with features like model year, brand, and speed.



- `__init__(self, yearmodel, make)` creates a new car object with the given year, model, and make.

- `accelerate(self)` is a function that can helps to increase the car's speed by 5.

- `brake(self)` this function helps to reduce the car's speed by 5.

- `get_speed(self)` returns the car's current speed.

### Pet Class
This code defines Pet, a simple application which enables users to input data regarding their pets and displays the information —name, animal type, and age . The Pet class is used to store and retrieve pet information, and the tkinter library is used to create the GUI.


-  `__init__(self)` this method creates a new pet object using the default values for name, animal type, and age.
- `set_name(self, name)` sets the name of the pet.
- `set_animal_type(self, animal_type)` sets the animal type of the pet.
- ` set_age(self, age)` sets the age of the pet.


## Guide

- To view the program's visuals, use pip install at the terminal to install pyfiglet and terminal color. Also import tkinkter to see the output display of this codes.

```bash
pip install pyfiglet
```

```bash
pip install termcolor
```

```bash
pip install tk
```

Note: You need to install first the pyfiglet, terminalcolor, and tkinkter to run this program properly and to not encounter an error.


## 🔗 Video Presentation

- Here's the video presentation of my output.

```bash
https://drive.google.com/drive/u/0/folders/1ElnP8yLUY3_-jpM8r5CR2uYzzRqZIqjU
```
