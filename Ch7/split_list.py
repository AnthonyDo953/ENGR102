# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 7.19 Split List
# Date: 02 October 2025

# Get the string of integers
numString = input("Enter numbers: ")

numList = [int(num) for num in numString.split()]

sumLeft = 0
sumRight = 0

# Make the right sum the sum of the entire list
for i in range(len(numList)):
    sumRight += numList[i]

splitLeft = []
splitRight = []

# Compare the left and right sums by adding an integer from the list to the left sum and subtracting that same integer from the right sum
for i in range(len(numList)):
    sumLeft += numList[i]
    sumRight -= numList[i]
    # If there is an equal split then print it out and stop the loop
    if sumLeft == sumRight:
        splitLeft = numList[0:i+1]
        splitRight = numList[i+1:]
        print(f"Left: {splitLeft}")
        print(f"Right: {splitRight}")
        print(f"Both sum to {sumLeft}")
        break
    # If the left sum gets bigger than the right, there is no equal split
    elif sumLeft > sumRight:
        print("Cannot split evenly")
        break