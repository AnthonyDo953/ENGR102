# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 7.20 Kaprekar's Constant
# Date: 02 October 2025

# Get a 4 digit integer and convert to a string
numInit = str(input("Enter a four-digit integer: "))

num = numInit
iterations = 0

# Do Kaprekar's routine until it reaches 6174
while num != 6174 and num != 0:
    print(f"{num} < ", end = "")
    iterations += 1

    # Convert it into a string for sorting
    num = str(num)
    num = num.zfill(4)

    # Create a list of digits
    digitList = list(num)

    # Sort them in ascending order
    asc = int("".join(sorted(digitList)))
    # Sort them in descending order
    desc = int("".join(sorted(digitList, reverse = True)))

    num = desc - asc

# If the routine works then it will end with Kaprekar's constant or 0
print(f"{num}")

print(f"{numInit} reaches {num} via Kaprekar's routine in {iterations} iterations")