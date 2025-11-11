# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Michaela Gutermuth
# Simon O'Brien
# Anthony Do
# Will Gipson
# Section: 217
# Assignment: 11.9 Passport Checker
# Date: 10 11 2025

file = input("Enter the name of the file: ")
outfile = open("valid_passports.txt", 'w')

with open(file, 'r') as scannedPassports:

    passport = {}
    requiredFields = ["iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    valid = True
    format = []

    for line in scannedPassports:

        if line != "" and line != "\n":

            format.append(line)

            line = line.replace("\n", "")

            line = line.split(" ") # [pid:827837505, byr:1976]

            for i in range(len(line)): 
                line[i] = line[i].split(":") # [[pid, 827837505], [byr,1976]]

            for item in line:
                # print(item)
                passport.update({item[0]: item[1]})

        else:

            for field in requiredFields:
                if field not in passport.keys():
                    valid = False

            if valid:
                print(format)
                for originalLine in format:
                    outfile.write(originalLine + "\n")

            format.clear()
            passport.clear()
            valid = True

        
                


