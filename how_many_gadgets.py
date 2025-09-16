# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 4.20 How Many Gadgets
# Date: 13 September 2025

days = int(input("Please enter a positive value for day: "))

numOfGadgets = 0
valid = True

# Check if it is a valid input 
if days < 0:
    valid = False
# Calculate for when the production rate is constant
elif 0 <= days <= 10:
    numOfGadgets = days * 10
# Calculate for when the production rate starts increasing by 1 each day
elif days <= 50:
    numOfGadgets = 100 + (days + 11)  * (days - 10) / 2
# Calculate for when the production rate stays at 50
elif days <= 100:
    numOfGadgets = 1320 + (days - 50) * 50
# Stop the production after day 101
else:
    numOfGadgets = 3820

numOfGadgets = int(numOfGadgets)

if (valid):
    print(f"The sum total number of  gadgets produced on day {days} is {numOfGadgets}")
else:
    print(f"You entered an invalid number!")

