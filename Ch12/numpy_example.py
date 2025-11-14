# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Michaela Gutermuth
# Simon O'Brien
# Anthony Do
# Will Gipson
# Section: 217
# Assignment: Lab Topic 12 Numpy Example
# Date: 10 11 2025

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

a = np.arange(12).reshape(3, 4)
print(f"A = {a}\n")

b = np.arange(8).reshape(4,2)
print(f"B = {b}\n")

c = np.arange(6).reshape(2,3)
print(f"C = {c}\n")

d = np.matmul(a, b) # Can use dot for 2D arrays instead of matmul
d = np.matmul(d,c)

print(f"D = {d}\n")

dT = np.transpose(d)

print(f"D^T = {dT}\n")

e = np.sqrt(d) / 2

print(f"E = {e}\n")

