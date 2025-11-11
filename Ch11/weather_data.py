# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 11.17 Loan Calculator
# Date: 10 November 2025

with open("WeatherDataCLL.csv", 'r') as weather:
    
    nextLine = weather.readline()
    nextLine = weather.readline()
    maxTemp = 0
    minTemp = 100

    while nextLine != "":
        nextLine = nextLine.split(",")

        if nextLine[8] != "" and nextLine[8] != "\n" and int(nextLine[8]) > maxTemp:
            maxTemp = int(nextLine[8])

        if nextLine[9] != "" and nextLine[9] != "\n"and int(nextLine[9]) < minTemp:
            minTemp = int(nextLine[9])

        nextLine = weather.readline()

print(f"10-year maximum temperature: {maxTemp} F")
print(f"10-year minimum temperature: {minTemp} F")

monthDic = {"January": [1,31], "February": [2,28], "March": [3,31], "April": [4,30], "May": [5,31], "June": [6,30], "July": [7,31], "August": [8,31], "September": [9,30], "October": [10,31], "November": [11,30], "December": [12,31]}

month = input("Please enter a month: ")
year = input("Please enter a year: ")
daysInMonth = monthDic[month][1]
dayCount = 1
sumP = 0
sumT = 0
sumWB = 0
sumDP = 0
sumRH = 0
sumWS = 0
daysP = 0
# weatherAvg = [sumP, sumT, sumWB, sumDP, sumRH, sumWS, daysP]

with open("WeatherDataCLL.csv", 'r') as weather:
    
    nextLine = weather.readline()
    nextLine = weather.readline()

    # Do getting
    for day in weather:
        day = day.split(",")
        date = day[0].split("/")

        if int(date[0]) == monthDic[month][0] and date[2] == year:
            if date[1] == daysInMonth:
                sumP += float(day[2])
                sumT += int(day[7])
                sumWB += int(day[3])
                sumDP += int(day[1])
                sumRH += int(day[6])
                sumWS += float(day[4])
                if day[5] != '0':
                    daysP += 1
                break
            else:
                sumP += float(day[2])
                sumT += int(day[7])
                sumWB += int(day[3])
                sumDP += int(day[1])
                sumRH += int(day[6])
                sumWS += float(day[4])
                if day[5] != '0':
                    daysP += 1
                
print(f"For {month} {year}:")
print(f"Mean average daily pressure: {sumP / daysInMonth:.2f} in Hg")    
print(f"Mean average daily temperature: {sumT / daysInMonth:.1f} F")
print(f"Mean average daily wet bulb temperature: {sumWB / daysInMonth:.1f} F")
print(f"Mean average daily dew point: {sumDP / daysInMonth:.1f} F")
print(f"Mean average daily relative humidity: {sumRH / daysInMonth:.1f}%")
print(f"Mean average daily wind speed: {sumWS / daysInMonth:.2f} mph")
print(f"Percentage of days with precipitation: {daysP / daysInMonth * 100:.1f}%")
