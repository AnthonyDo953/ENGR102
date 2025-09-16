# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 4.21 Calculate Roots
# Date: 13 September 2025

import math

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

root1 = 0
root2 = 0
numOfRoots = 0

# If A is 0 there is one root
if A == 0 and B != 0:
    numOfRoots = 1
    root1 = -1 * C / B
    print(f"The root is x = {root1}")
# If A and B are 0 this is not valid
elif A == B == 0:
    print(f"You entered an invalid combination of coefficients!")
# If A does not equal 0 there are two roots
else:
    if B ** 2 - (4 * A * C) < 0:
        numOfRoots = 2
        iValue = math.sqrt(abs(B ** 2 - (4 * A * C))) / (2 * A)
        root1 = (-1 * B) / (2 * A)
        print(f"The roots are x = {root1} + {iValue}i and x = {root1} - {iValue}i")
    else:
        numOfRoots = 2
        root1 = (-1 * B + math.sqrt(B ** 2 - (4 * A * C))) / (2 * A)
        root2 = (-1 * B - math.sqrt(B ** 2 - (4 * A * C))) / (2 * A)
        if root1 == root2:
            print(f"The root is x = {root1}")
        elif root1 > root2:
            print(f"The roots are x = {root1} and x = {root2}")
        else:
            print(f"The roots are x = {root2} and x = {root1}")
