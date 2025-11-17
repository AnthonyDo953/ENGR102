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
import matplotlib.pyplot as plt

# Graph 1

# Get the domain for x
x = np.linspace(-2, 2)
f1 = 2
f2 = 6

# Make equations for both values of f
para1 = 1 / (4 * f1) * x**2
para2 = 1 / (4 * f2) * x**2

# Plot both equations with a specified line width and label for the legend
plt.plot(x, para1, "r", linewidth = 2.0, label = "f = 2")
plt.plot(x, para2, "b", linewidth = 6.0, label = "f = 6")

# Label the x and y axes
plt.xlabel('x')
plt.ylabel('y')
# Give a title to the graph
plt.title("Parabola plots with varying focal lengths")
# Add a legend to the plot specifying which graph is which
plt.legend()

plt.show()

# Graph 2

# Create a new figure so that it plots to a different graph
plt.figure(figsize = (6,5))

# Set the domain from -4 to 4 and specify to take 25 evenly spaced x values from that domain
x = np.linspace(-4, 4, 25)

# Make equation
poly = 2 * x**3 + 3 * x**2 - 11 * x - 6

# Plot the equation, specifying marker type, color, and marker size
# Linestyle at none to make it the individual points rather than a continuous line
# Markerfacecolor at none to make the points hollow
plt.plot(x, poly, c = 'red', marker = '*', linestyle = 'none', markerfacecolor = 'none', markersize = 10)

# Set the y axis to intervals of 25
plt.yticks(np.arange(-50, 126, 25))      # ticks from -50 to 125, step 25

# Label x and y axes and title the graph
plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Plot of cubic polynomial")

plt.show()

# Graph 3

# New graph
plt.figure()

# Set domain from -2pi to 2pi
x = np.linspace(-2 * np.pi, 2 * np.pi)

# Create both functions
sine = np.sin(x)
cosine = np.cos(x)

# Create first subplot and plot cos(x)
plt.subplot(211)
plt.plot(x, cosine, c = 'r', label = 'cos(x)')

# Adjust the formatting and adds labels
plt.gca().set_xticklabels([])  # keeps the ticks but hides numbers
plt.yticks(np.arange(-1, 1.01, 1))      # ticks from -1 to 1, step 1
plt.ylabel('y=cos(x)')
plt.grid(True)
plt.legend(loc = 'lower right')

# Create second subplot and plot sin(x)
plt.subplot(212)
plt.plot(x, sine, c = 'gray', label = 'sin(x)')

# Adjust formatting
plt.yticks(np.arange(-1, 1.01, 1))      # ticks from -1 to 1, step 1
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.grid(True)
plt.legend()

# Add title to the whole figure instead of individual graphs 
plt.suptitle("Plot of cos(x) and sin(x)")

plt.show()

