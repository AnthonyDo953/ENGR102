# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 2.10
# Date: 02 September 2025

# Given variables
startingTime = 30
endingTime = 60

x1 = 8
y1 = 6
z1 = 7
x2 = -5
y2 = 30
z2 = 9
t1 = 12
t2 = 85

t = 30.0

# Calculate the time in between each computation
intervalTime = (endingTime - startingTime) / 4

# Get the slope of each position variable
slopeX = (x2 - x1) / (t2 - t1)
slopeY = (y2 - y1) / (t2 - t1)
slopeZ = (z2 - z1) / (t2 - t1)

# Print the calculated position at each interval
for i in range(1,6):
    print(f"At time {t} seconds:")
    print(f"x{i} = {slopeX * (t - t1) + x1} m")
    print(f"y{i} = {slopeY * (t - t1) + y1} m")
    print(f"z{i} = {slopeZ * (t - t1) + z1} m")
    if (i < 5):
        print("-----------------------")
    t += intervalTime




