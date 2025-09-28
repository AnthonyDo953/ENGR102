# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 6.16 Howdy Whoop
# Date: 27 September 2025

# Get integers to divide each number from 1-100
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

# Do the calculation for each number 1-100
for i in range(1, 101):
    # If divisible by both integers print Howdy Whoop
    if i % int1 == 0 and i % int2 == 0:
        print("Howdy Whoop")
    # If only divisible by the first input integer print Howdy
    elif i % int1 == 0:
        print("Howdy")
    # If only divisible by the second input integer print Whoop
    elif i % int2 == 0:
        print("Whoop")
    # Print the number if not divisible by either integer
    else:
        print(i)