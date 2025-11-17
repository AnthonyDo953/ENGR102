# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab Topic 12 Pretty Plot
# Date: 17 November 2025

import numpy as np
import matplotlib.pyplot as plt

v = np.array([[0], 
             [1]])

M = np.array([[1.02, 0.095],
     [-0.095, 1.02]])

newPoint = v

for i in range(250):
    newPoint = np.matmul(M, newPoint)
    print(f"x = {newPoint[0][0]} y = {newPoint[1][0]}")
    plt.plot(newPoint[0][0], newPoint[1][0], 'o')

plt.show()
