# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 1.12
# Date: 27 August 2025

import math

print("Reynolds number is" , ( (9.0 * 0.875) / 0.0015))

print("Wavelength is", 2 * 0.029 * math.sin(math.radians(35)), "nm")

# 10 days 100 barrels/day decline rate of 2/day hyperbolic constant 0.8
print("Production rate is", str(100 * math.pow(1 + 0.8 * 2 * 10, -1 / 0.8)) + "7 barrels/day")

# Initial mass 11000kg Final mass 8300 kg exhaust velocity 2029 m/s
print("Change of velocity is", 2029 * math.log(11000/8300, math.e), "m/s")