# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 6.19.1 Juggling Sequence
# Date: 27 September 2025

from math import *

# Get the number to do the Juggler sequence on
juggle = int(input("Enter a positive integer: "))

# Print out the Juggler sequence
print(f"The Juggler sequence starting at {juggle} is: ")

# Print out the first number in the Juggler sequence
print(juggle, end = "")

# Track how many times we juggle
iterations = 0

# Juggle until the number is 1
while juggle != 1:
    # Add 1 juggle
    iterations += 1
    print(", ", end = "")
    # Do floor of the square root if the number is even
    if (juggle % 2 == 0):
        juggle = int(sqrt(juggle) // 1)
    # Do floor of power of 3/2 if the number is odd
    else:
        juggle = int(juggle ** (3/2) // 1)
    # Print out the current number that is being juggled
    print(juggle, end = "")

# Print out how many times the user input integer had to be juggled
print(f"\nIt took {iterations} iterations to reach 1")