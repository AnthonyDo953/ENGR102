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

# Makes a matrix from 0 to 11 with 3 rows and 4 columns
a = np.arange(12).reshape(3, 4)
print(f"A = {a}\n")

# Makes a matrix from 0 to 7 with 4 rows and 2 columns
b = np.arange(8).reshape(4,2)
print(f"B = {b}\n")

# Makes a matrix from 0 to 5 with 2 rows and 3 columns
c = np.arange(6).reshape(2,3)
print(f"C = {c}\n")

# Does matrix multiplication between matrix A, B, and C
d = np.matmul(np.matmul(a, b), c) # Can use dot for 2D arrays instead of matmul
print(f"D = {d}\n")

# Transposes matrix D
# Transposing a matrix is flipping it on its diagonal, ie. swapping its rows and columns
dT = np.transpose(d)
print(f"D^T = {dT}\n")

# Computing the square root of matrix D and dividing by 2
e = np.sqrt(d) / 2
print(f"E = {e}\n")

