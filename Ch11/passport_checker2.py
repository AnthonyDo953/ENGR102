# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Michaela Gutermuth
# Simon O'Brien
# Anthony Do
# Will Gipson
# Section: 217
# Assignment: 11.10 Passport Checker B
# Date: 10 11 2025

# Take a field on a passport and its associated value and then check if it is valid
# Return True if it is and False otherwise
def validField(field, value):
    match field:
        case "iyr":
            if len(value) == 4 and 2015 <= int(value) <= 2025:
                return True
            else:
                return False
        case "eyr":
            if len(value) == 4 and 2025 <= int(value) <= 2035:
                return True
            else:
                return False
        case "hgt":
            unit = value[-2:]
            if unit == "cm" and 150 <= int(value.replace("cm", "")) <= 193:
                return True
            elif unit == "in" and 59 <= int(value.replace("in", "")) <= 76:
                return True
            else:
                return False
        case "hcl":
            if value[0] == "#" and len(value) == 7:
                for char in value:
                    if char not in "#1234567890abcdef":
                        return False
                return True
            return False
        case "ecl":
            validEcl = ["amb", "blu","brn", "gry", "grn", "hzl", "oth"]
            if value in validEcl:
                return True
            else: 
                return False
        case "pid":
            if len(value) == 9:
                for char in value:
                    if char not in "0123456789":
                        return False
                return True
        case "cid":
            value = value.lstrip("0")
            if len(value) == 3:
                return True
            else:
                return False
        case _:
            return False


# Get file name and make file to write to
file = input("Enter the name of the file: ")
outfile = open("valid_passports2.txt", 'w')

# Open and read input file
with open(file, 'r') as scannedPassports:

    # Get all lines to check if last line in file later
    lines = scannedPassports.readlines()

    # Initialize variables 
    passport = {}
    requiredFields = ["iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    valid = True
    validPassports = 0
    format = []

    # Go through each line in the file
    for i, line in enumerate(lines):

        # Get rid of \n at the end of each line
        line = line.strip()

        # Last line
        if i == len(lines) - 1:
            
            # Store original line for writing later
            format.append(line)

            # Split by whitespace to get each key:pair value
            line = line.split(" ") 

            # Split by : to get each key: pair value separated
            for i in range(len(line)): 
                line[i] = line[i].split(":") 

            # Put each key:pair data value into a dictionary
            for item in line:
                passport.update({item[0]: item[1]})
            
            # Passport is not valid if it doesn't contain all required fields or the value does not follow the rules
            for field in requiredFields:
                if field not in passport.keys():
                    valid = False
                    break
                elif not validField(field, passport[field]):
                    valid = False
                    break

            # If a valid passport, add 1 to counter and write it 
            # Since this the last line track writing to not add an extra empty line at the end of the file
            if valid:
                validPassports += 1
                for i, originalLine in enumerate(format):
                    if i == len(format) - 1:
                        outfile.write(originalLine)
                        break
                    else:
                        outfile.write(originalLine + "\n")


        # Not last line
        else:

            # If not empty line
            if line != "" and line != "\n":
                
                # Store original line for writing later
                format.append(line)

                # Split by whitespace to get each key:pair value
                line = line.split(" ") 

                # Split by : to get each key: pair value separated
                for i in range(len(line)): 
                    line[i] = line[i].split(":") 

                # Put each key:pair data value into a dictionary
                for item in line:
                    passport.update({item[0]: item[1]})

            # If it is an empty line, that means the data for that passport is finished
            else:

                # Passport is not valid if it doesn't contain all required fields
                for field in requiredFields:
                    if field not in passport.keys():
                        valid = False
                        break
                    elif not validField(field, passport[field]):
                        valid = False
                        break


                # If a valid passport, add 1 to counter and write it 
                if valid:
                    validPassports += 1
                    for originalLine in format:
                        outfile.write(originalLine + "\n")
                    outfile.write("\n")
                        
                # When finished with one passport, clear all relevant variables to use with the next passport
                format.clear()
                passport.clear()
                valid = True

# Close file
outfile.close()

print(f"There are {validPassports} valid passports")