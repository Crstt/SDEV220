# SDEV 220 - CatalanoMatteo_M03_01.py - M03 Lab - Case Study: Lists, Functions, and Classes
# Catalano Matteo
# 31/03/2023
# This Python program defines two classes, Vehicle and Automobile, where Automobile inherits from Vehicle. 
# The Vehicle class has an attribute for the type of vehicle, while the Automobile class adds attributes for year, make, model, number of doors, and type of roof. 
# The program prompts the user to enter information about a car, creates an instance of the Automobile class with the user input, and then outputs the information in an easy-to-read format.
# Variables descriptions:
# car_type: a string variable that stores the type of vehicle entered by the user.
# year: a string variable that stores the year of the vehicle entered by the user.
# make: a string variable that stores the make of the vehicle entered by the user.
# model: a string variable that stores the model of the vehicle entered by the user.
# doors: a string variable that stores the number of doors of the vehicle entered by the user.
# roof: a string variable that stores the type of roof of the vehicle entered by the user.
# car: an instance of the Automobile class created using the user input data.
# Vehicle: a class that defines a vehicle and has an attribute for the type of vehicle.
# utomobile: a class that inherits from the Vehicle class and adds attributes for year, make, model, number of doors, and type of roof.

# Define the Vehicle class with a constructor that sets the vehicle type attribute
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile class that inherits from Vehicle and adds more attributes
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Call the constructor of the superclass using super()
        super().__init__(vehicle_type)
        # Set the additional attributes specific to Automobile
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Prompt the user to enter information about the car
car_type = input("Enter the type of vehicle (car, truck, plane, boat, or broomstick): ")
year = input("Enter the year of the vehicle: ")
make = input("Enter the make of the vehicle: ")
model = input("Enter the model of the vehicle: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an instance of the Automobile class using the user input
car = Automobile(car_type, year, make, model, doors, roof)

# Print the information about the car in an easy-to-read format
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)