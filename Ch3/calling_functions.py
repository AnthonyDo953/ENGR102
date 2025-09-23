# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 3.22 Calling Functions
# Date: 6 September 2025

import math

from math import *

# Given function from assignment
# Prints the area of certain shapes given a side length
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# List of the shapes to be calculated areas for
shapeList = ["triangle", "square", "pentagon", "hexagon", "dodecagon"]

# Get user input for the side length
side = float(input("Please enter the side length: \n"))

# Calculate the area of a given shape using the side length
def calculateArea(shape, side):
    match shape:
        case "triangle":
            return math.sqrt(3) / 4 * side ** 2
        case "square":
            return side ** 2
        case "pentagon":
            return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
        case "hexagon":
            return ((3 * math.sqrt(3)) / 2) * side ** 2
        case "dodecagon":
            return 3 * (2 + math.sqrt(3)) * side ** 2

# Print out the area for all the shapes
printresult(shapeList[0], side, calculateArea(shapeList[0], side))
printresult(shapeList[1], side, calculateArea(shapeList[1], side))
printresult(shapeList[2], side, calculateArea(shapeList[2], side))
printresult(shapeList[3], side, calculateArea(shapeList[3], side))
printresult(shapeList[4], side, calculateArea(shapeList[4], side))




