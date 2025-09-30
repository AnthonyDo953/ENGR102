# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: 6.11 Pyramid area Team
# Date: 29 09 2025

sl = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))
x =n
area = 0

#looping
while n>0:
    area += (n*(sl**2)*4) + (n*sl)**2 
    area -= ((n-1)*sl)**2
    n-=1

print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")