# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 4.19 Largest Number
# Date: 13 September 2025

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

largest = 0
middle = 0
smallest = 0

# Check if number 1 is larger than number 2 and 3
if num1 > num2 and num1 > num3: 
    largest = num1 
# Check if number 2 is larger than number 1 and 3
elif num2 > num1 and num2 > num3:
    largest = num2 
# Number 3 is the largest
else:
    largest = num3

print(f"The largest number is {largest}")