# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Gipson
#               Anthony Do
#               Simon O'Brien
#               Michaela Gutermuth
# Section:      217
# Assignment:   THE ASSIGNMENT NUMBER (Lab Topic 3 Team Unit Conversions)
# Date:         04 09 2025

input = float(str(input("Please enter the quantity to be converted:")))
#a lbs to N
newtons = input * (4.4482216153)
print(f"{input:.2f} pounds force is equivalent to {newtons:.2f} newtons")
#b m to ft
feet = input * 3.28084
print(f"{input:.2f} meters is equivalent to {feet:.2f} feet")
#c atmosphere to kpa
kpa = input * 101.325
print(f"{input:.2f} atmospheres is equivalent to {kpa:.2f} kilopascals")
# d watts to btu/hr
btu = input * 3.412141633
print(f"{input:.2f} watts is equivalent to {btu:.2f} BTU per hour")
# e liters/sec to gallons/min
gallons_per_min = input * 15.850323074494
print(f"{input:.2f} liters per second is equivalent to {gallons_per_min:.2f} US gallons per minute")
# f degrees C to F
f = (input * 9/5) +32
print(f"{input:.2f} degrees Celsius is equivalent to {f:.2f} degrees Fahrenheit")