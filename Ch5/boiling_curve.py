# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 5.5 Boiling Curve
# Date: 13 September 2025

from math import *

# Get the user input for the excess temperature to be used to calculate the surface heat flux at 1 atm
excessTemperature = float(input("Enter the excess temperature: "))

# Values for the first point on the graph 
AX = 1.3
AY = 1000
# Values for the second point on the graph 
BX = 5
BY = 7000
# Values for the third point on the graph 
CX = 30
CY = 1.5 * (10 ** 6)
# Values for the fourth point on the graph 
DX = 120
DY = 2.5 * (10 ** 4)
# Values for the fifth point on the graph 
EX = 1200
EY = 1.5 * (10 ** 6)

# Calculate the slope of the line segment AB 
slopeAB = log(BY / AY) / log(BX / AX)
# Calculate the slope of the line segment BC
slopeBC = log(CY / BY) / log(CX / BX)
# Calculate the slope of the line segment CD 
slopeCD = log(DY / CY) / log(DX / CX)
# Calculate the slope of the line segment DE 
slopeDE = log(EY / DY) / log(EX / DX)

# Check if the input excess temperature is a valid input that we can calculate with
# If it's not valid then return a message stating so
if excessTemperature > 1.3 and excessTemperature < 1200:

    # Check if we use the linear interpolation between A and B
    if excessTemperature < 5:
        surfaceHeatFlux = round(AY * (excessTemperature / AX) ** slopeAB)

    # Check if we use the linear interpolation between B and C
    elif excessTemperature < 30: 
        surfaceHeatFlux = round(BY * (excessTemperature / BX) ** slopeBC)

    # Check if we use the linear interpolation between C and D
    elif excessTemperature < 120:
        surfaceHeatFlux = round(CY * (excessTemperature / CX) ** slopeCD)

    # Check if we use the linear interpolation between D and E
    elif excessTemperature < 1200:
        surfaceHeatFlux = round(DY * (excessTemperature / DX) ** slopeDE)

    # Print out the calculated surface heat flux after using the appropriate linear interpolation formula
    print(f"The surface heat flux is approximately {surfaceHeatFlux} W/m^2")

else: 
    print("Surface heat flux is not available")
