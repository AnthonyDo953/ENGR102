# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 3.21 Using Input
# Date: 6 September 2025

import math

print("This program calculates the Reynolds number given velocity, length, and viscosity")

# Get user input for velocity, length, and viscosity
velocity = float(input("Please enter the velocity (m/s): \n"))
linearDimension = float(input("Please enter the length (m): \n"))
kinematicViscosity = float(input("Please enter the viscosity (m^2/s): \n"))


# Calculate the Reynolds number based on given variables
print(f"Reynolds number is {(velocity * linearDimension) / kinematicViscosity:.0f}\n")

print("This program calculates the wavelength given distance and angle")

# Get user input for distance and angle
distance = float(input("Please enter the distance (nm): \n"))
angle = float(input("Please enter the angle (degrees): \n"))

# Calculate the wavelength based on given variables
print(f"Wavelength is {(2 * distance * math.sin(math.radians(angle))):.4f} nm\n")

print("This program calculates the production rate given time, initial rate, and decline rate")

# Get user input for days, initial rate, and decline rate
days = float(input("Please enter the time (days): \n"))
initialRate = float(input("Please enter the initial rate (barrels/day): \n"))
declineRate = float(input("Please enter the decline rate (1/day): \n"))
hyperbolicConstant = 0.8

# Calculate the production rate based on given variables
print(f"Production rate is {(initialRate * math.pow(1 + hyperbolicConstant * declineRate * days, -1 / hyperbolicConstant)):.2f} barrels/day\n")

print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")

# Get user input fot initial mass, final mass, and exhaust velocity
initialMass = float(input("Please enter the initial mass (kg): \n"))
finalMass = float(input("Please enter the final mass (kg): \n"))
exhaustVelocity = float(input("Please enter the exhaust velocity (m/s): \n"))

# Initial mass 11000kg Final mass 8300 kg exhaust velocity 2029 m/s
print(f"Change of velocity is {(exhaustVelocity * math.log(initialMass / finalMass, math.e)):.1f} m/s")