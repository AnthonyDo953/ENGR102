# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 11.15 Barcode Checker
# Date: 10 November 2025

file = input("Enter the name of the file: ")
outfile = open("valid_barcodes.txt", 'w')

# Do file stuff
with open(file, "r") as barcodes:
    validBarcodes = 0

    for barcode in barcodes:
        firstGroup = 0
        secondGroup = 0
        count = 1
        
        for char in barcode:
            if char != "\n" and count < 13:
                if count % 2 != 0:
                    firstGroup += int(char)
                else:
                    secondGroup += int(char)
            count += 1

        if (10 - ((secondGroup * 3 + firstGroup) % 10)) == int(barcode[12]):
            validBarcodes += 1
            outfile.write(barcode)

print(f"There are {validBarcodes} valid barcodes")
    

    

    
            