# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 2.11
# Date: 28 August 2025

# Set variables
x = 1
y = 10
z = 0

# Make add 1 to z
z += x
print(z)

# Make y = 20 and add x to get to 29
x += 1
y *= x
z += y
z += x
z += x
z += x
z += x
print(z)

# Reset variables
x = 1
y = 10
z = 0

# Add the two to the end
z += x
z += x

# Get to 100 with y
x = y
y *= x
z += y
print(z)

# Reset some variables
y = 10
z = 0

# Get y to the right number of digits
x = y
y *= x
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z += y
print(z)

# Reset some variables
y = 10
z = 0

# Get the thousands
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y

# Reset needed variables
x = 1
y = 10

# Get the hundreds
x = y
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y

# Reset some needed variables
x = 1
y = 10

# Get the tens
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y

# Reset x and get the ones
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)