# Reggie Brown
# calculate the volume of a cylinder program
import math
# Constants
PI = 3.14
# Get user input
radius = float(input("Please enter the radius of the cylinder: "))
height = float(input("Please enter the height of the cylinder: "))

volume = PI * pow(radius, 2) * height

print("The volume of the cylinder is: " + str(volume))