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

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.00, 2.00, 0.01)
f = 2

y = 1 / (4 * f) * x ** 2

plt.plot(x, y, "r")

plt.show()

