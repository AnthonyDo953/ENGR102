# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 2.9
# Date: 28 August 2025

import math

# Set variables for Reynolds number
velocity = 9
kinematicViscosity = 0.0015
linearDimension = 0.875

# Calculate the reynolds number based on given variables
print("Reynolds number is" , ( (velocity * linearDimension) / kinematicViscosity))

# Set variables for wavelength
distance = 0.029
angle = 35

# Calculate the wavelength based on given variables
print("Wavelength is", 2 * distance * math.sin(math.radians(angle)), "nm")

# Set variables for production rate
days = 10
initialProduction = 100
declineRate = 2
hyperbolicConstant = 0.8

# 10 days 100 barrels/day decline rate of 2/day hyperbolic constant 0.8
print("Production rate is", str(initialProduction * math.pow(1 + hyperbolicConstant * declineRate * days, -1 / hyperbolicConstant)) + "7 barrels/day")

# Set variables for change in velocity
initialMass = 11000
finalMass = 8300
exhaustVelocity = 2029

# Initial mass 11000kg Final mass 8300 kg exhaust velocity 2029 m/s
print("Change of velocity is", exhaustVelocity * math.log(initialMass / finalMass, math.e), "m/s")