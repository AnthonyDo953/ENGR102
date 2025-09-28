# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 6.17.1 Computing Sums
# Date: 27 September 2025

# Get integers to do calculate sum with
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

# Create a variable to store the sum of all the integers between the two user input integers
sum = 0

# For each number in between the two user input integers add it to a sum variable 
for i in range(int1, int2 + 1):
    sum = sum + i

# Print out the result of the calculation
print(f"The sum of all integers from {int1} to {int2} is {sum}")