time = input("Enter the time: ")
clockType = int(input("Choose the clock type (12 or 24): "))

validChars = "abcdeghkmnopqrsuvwxyz@$&*="
character = input("Enter your preferred character: ")

while not character in validChars:
    character = input("Character not permitted! Try again: ")

timeMilitary = time.split(":")
if clockType == 12 and int(timeMilitary[0]) > 12:
    time = str(int(timeMilitary[0]) - 12) + ":" + timeMilitary[1] + "PM"
elif clockType == 12 and int(timeMilitary[0]) == 0:
    time = "12" + ":" + timeMilitary[1] + "AM"
else:
    time += "AM"
time = list(time)

numbers = {0: [['0',' ','0',' ','0'], ['0',' ',' ',' ','0'], ['0',' ',' ',' ','0'],['0',' ',' ',' ','0'], ['0',' ','0',' ','0']],
           1: [[' ',' ','1',' ',' '], ['1',' ','1',' ',' '], [' ',' ','1',' ',' '],[' ',' ','1',' ',' '], ['1',' ','1',' ','1']],
           2: [['2',' ','2',' ','2'], [' ',' ',' ',' ','2'], ['2',' ','2',' ','2'],['2',' ',' ',' ',' '], ['2',' ','2',' ','2']],
           3: [['3',' ','3',' ','3'], [' ',' ',' ',' ','3'], ['3',' ','3',' ','3'],[' ',' ',' ',' ','3'], ['3',' ','3',' ','3']],
           4: [['4',' ',' ',' ','4'], ['4',' ',' ',' ','4'], ['4',' ','4',' ','4'],[' ',' ',' ',' ','4'], [' ',' ',' ',' ','4']],
           5: [['5',' ','5',' ','5'], ['5',' ',' ',' ',' '], ['5',' ','5',' ','5'],[' ',' ',' ',' ','5'], ['5',' ','5',' ','5']],
           6: [['6',' ','6',' ','6'], ['6',' ',' ',' ',' '], ['6',' ','6',' ','6'],['6',' ',' ',' ','6'], ['6',' ','6',' ','6']],
           7: [['7',' ','7',' ','7'], [' ',' ',' ',' ','7'], [' ',' ',' ',' ','7'],[' ',' ',' ',' ','7'], [' ',' ',' ',' ','7']], 
           8: [['8',' ','8',' ','8'], ['8',' ',' ',' ','8'], ['8',' ','8',' ','8'],['8',' ',' ',' ','8'], ['8',' ','8',' ','8']], 
           9: [['9',' ','9',' ','9'], ['9',' ',' ',' ','9'], ['9',' ','9',' ','9'],[' ',' ',' ',' ','9'], ['9',' ','9',' ','9']],
           ":": [[' ',' ',' ',' ',' '], [' ',' ',':',' ',' '], [' ',' ',' ',' ',' '],[' ',' ',':',' ',' '], [' ',' ',' ',' ',' ']],
           "A": [[' ',' ','A',' ',' '], ['A',' ',' ',' ','A'], ['A',' ','A',' ','A'],['A',' ',' ',' ','A'], ['A',' ',' ',' ','A']],
           "P": [['P',' ','P',' ','P'], ['P',' ',' ',' ','P'], ['P',' ','P',' ','P'],['P',' ',' ',' ',' '], ['P',' ',' ',' ',' ']],
           "M": [['M',' ',' ',' ','M'], ['M','M',' ','M','M'], ['M',' ','M',' ','M'],['M',' ',' ',' ','M'], ['M',' ',' ',' ','M']]}

clock = [[] for i in range(5)]

for digit in time:
    if digit in "0123456789":
        for i in range(len(clock)):
            clock[i].append(numbers[int(digit)][i])
    elif digit in ":APM":
            for i in range(len(clock)):
                clock[i].append(numbers[digit][i])

for row in clock:
    for thing in row:
        for element in thing: 
            if character != "":
                if element != " " and not element in ":APM":
                    print(element.replace(element, character), end = "")
                else:
                    print(element, end = "")
            else:
                print(element, end = "")
        print("   ", end = "")
    print()
