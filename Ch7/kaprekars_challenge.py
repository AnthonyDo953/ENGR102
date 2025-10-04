# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 7.21.1 Kaprekar's Constant Challenge
# Date: 02 October 2025


iterations = 0

for i in range(10000):
    num = i
# Do Kaprekar's routine until it reaches 6174
    while num != 6174 and num != 0:
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

print(f"Kaprekar's routine takes {iterations} total iterations for all four-digit numbers")