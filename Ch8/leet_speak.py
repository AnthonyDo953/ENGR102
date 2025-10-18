# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 8.18.1 Leet Speak 
# Date: 17 October 2025

# Leet speak conversion
leet = {"a": "4", "e": "3", "o": "0", "s": "5", "t": "7"}

textToConvert = input("Enter some text: ")

# Put input into a list
textList = list(textToConvert)

leetText = ""

# If there is a conversion for leet add that conversion if not keep the same letter
for letter in textList:
    if letter in leet:
        leetText += leet[letter]
    else:
        leetText += letter

print(f'In leet speak, "{textToConvert}" is: \n{leetText}')