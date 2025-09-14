# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Willaim Gipson
#               Michaela Gutermuth
#               Simon O'Brien
#               Anthony Do
# Section:      217
# Assignment:   3.20 LAB: Still More Linear Interpolation
# Date:         09 09 2025

# Takes two points and makes a line
t1 = float(input("Enter time 1:"))
x1 = float(input("Enter the x position of the object at time 1:"))
y1 = float(input("Enter the y position of the object at time 1:"))
z1 = float(input("Enter the z position of the object at time 1:"))

t2 = float(input("Enter time 2:"))
x2 = float(input("Enter the x position of the object at time 2:"))
y2 = float(input("Enter the y position of the object at time 2:"))
z2 = float(input("Enter the z position of the object at time 2:"))

x_factor = (x2-x1)/(t2-t1)
y_factor = (y2-y1)/(t2-t1)
z_factor = (z2-z1)/(t2-t1)

i = 0

while i < 1.25:
    print(f"At time {t1+(t2-t1)*i:.2f} seconds the object is at ({x1+x_factor*i*(t2-t1):.3f}, {y1+y_factor*i*(t2-t1):.3f}, {z1+z_factor*i*(t2-t1):.3f})")
    i = i + .25