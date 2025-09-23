# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: Topic 2 Part 2
# Date: 02 09 2025

import math

#part 1

#given
t1=10
d1=2029
t2=55
d2=23029

#solve for
t_chosen=25

#math part1
slope = (d2-d1)/(t2-t1)

d3 = d1 + ((t_chosen - t1) * slope)

print(f"At time {t_chosen} seconds:")
print(f"For t = {t_chosen} minutes, the position p = {d3} kilometers")

#math part 2
t_chosen = 300

d3 = d1 + ((t_chosen - t1) * slope)
d4 = d3 % (2 * math.pi * 6745)

print("Part 2:")
print(f"For t = {t_chosen} minutes, the position p = {d4} kilometers")