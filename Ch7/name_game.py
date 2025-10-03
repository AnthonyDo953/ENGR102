# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 7.18.1 The Name Game
# Date: 02 October 2025

# Get the user's name
name = input("What is your name? ")

# Separate the name into characters
nameList = list(name)

vowelList = ["a", "e", "i", "o", "u", "y"]

# If the name starts with a vowel then make the first letter lowercase 
if nameList[0].lower() in vowelList:
    nameList[0] = nameList[0].lower()
# If the second letter is a vowel then only get rid of the first letter in the name
elif nameList[1] in vowelList:
    nameList = nameList[1:]
# If the second letter is a consonant get rid of both first and second letter
elif nameList[2] in vowelList:
    nameList = nameList[2:]
else: 
    nameList = nameList[3:]

# Do the name game
print(f"{name}, {name}, Bo-B{''.join(nameList)}")
print(f"Banana-Fana Fo-F{''.join(nameList)}")
print(f"Me Mi Mo-M{''.join(nameList)}")
print(f"{name}!")