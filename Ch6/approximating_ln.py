# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: 6.15 Approximating ln
# Date: 27 09 2025

from math import log

# Get the number that we are approximating ln for
x = float(input("Enter a value for x: "))

# Ask to input a different number if not in the correct range
while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))

# Get the tolerance that the user is allowing
tolerance = float(input("Enter the tolerance: "))

# Set the initial formula for ln approximation using taylor series
lnApprox = x - 1

i = 2

# Keep doing terms until below tolerance
while True:
    # Switch between subtracting and adding the term
    if i % 2 == 0:
        term = -(x - 1)**i / i
    else:
        term = (x - 1)**i / i

    if abs(term) < tolerance:
        break
    
    # Adding the term to the current approximation for ln
    lnApprox += term
    i += 1

# Find the difference between the actual value and approximation
difference = abs(log(x) - lnApprox)

print(f"ln({x}) is approximately {lnApprox}")
print(f"ln({x}) is exactly {log(x)}")
print(f"The difference is {difference}")