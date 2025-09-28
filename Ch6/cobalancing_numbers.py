# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 6.20.1 Co-balancing Numbers
# Date: 27 September 2025

# Get the number that we are checking co-balance for
cobalanceNumber = int(input("Enter a value for n: "))

# Stores the sum of the co-balance of the input integer
sumOfCobalance = 0
# Stores the sum of the r we are checking co-balance with
sumOfR = 0
# Stores the r value that we have
r = 0

# Get the sum of the integers between 1 and the input integer
for i in range (1, cobalanceNumber + 1):
    sumOfCobalance = sumOfCobalance + i

# Adding this to cobalanceNumber in calculations instead of changing or creating a new variable for cobalanceNumber
i = 1

# Find an r by getting the sum of the numbers after the input integer until it reaches the sum of the input integer or becomes larger
while sumOfR < sumOfCobalance:
    sumOfR += cobalanceNumber + i
    i += 1
    r += 1

# Print that the input integer is in fact a co-balancing number along with the r value associated with it if the two sums match
if sumOfCobalance == sumOfR:
    print(f"{cobalanceNumber} is a co-balancing number with r={r}")
# If the sum don't match then print out that it is not a co-balancing number
else:
    print(f"{cobalanceNumber} is not a co-balancing number")