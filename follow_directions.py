# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 1.13
# Date: 27 August 2025

import math

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")

print("My guess is 0")

x = 1

# Make x a 10th of the previous version
for i in range(8):
    print((1 - math.cos(x)) / (x**2))
    x = round(x * 0.1, i + 1)

print("")

print("My guess was ok.")