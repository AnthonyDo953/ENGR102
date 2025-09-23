# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: 4.18 Lab: Boolean Expressions
# Date: 14 09 2025
#

############ Part A ############

# Returns true if the string is in the list of accepted true values and false if not
def strToBool(str):
    return str in ["True", "T", "t"]

a = strToBool(input("Enter True or False for a: "))
b = strToBool(input("Enter True or False for b: "))
c = strToBool(input("Enter True or False for c: "))

############ Part B ############

print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############

XOR = (a or b) and (a != b)

print(f"XOR: {XOR}")

# Checks every case
# Probably a better way to check this but im dumb
oddTrue = (a and a != b and a != c) or (a and a == b and a == c) or (b and b != a and b != c) or (c and c != a and c != b)

print(f"Odd number: {oddTrue}")

print(f"Complex 1: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}")
print(f"Complex 2: {(not ((b or not c) and (not a or not c))) or (not (c or not (b and c)))  or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}")

simple1 = not b or (not a and b and not c)
simple2 = a or (not a and not b and c) 

print(f"Simple 1: {simple1}")
print(f"Simple 2: {simple2}")

