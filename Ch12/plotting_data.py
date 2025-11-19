# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab Topic 12 Plotting Data
# Date: 17 November 2025

import numpy as np
import matplotlib.pyplot as plt

# Open weather file
with open("WeatherDataCLL.csv", 'r') as weather:
    
    # Start reading data
    nextLine = weather.readline()
    nextLine = weather.readline()

    # Counter for date
    i = 1 

    # Setting lists that we use to plot
    x = []
    avgWetBulbTemp = []
    avgPressure = []
    avgWindSpeed = []
    avgRelativeHumidity = []
    avgDewPoint = []

    # Dictionary for storing weather data for variables below
    monthDicData = {"1": [[], [], [], []], "2": [[], [], [], []], "3": [[], [], [], []], "4": [[], [], [], []], "5": [[], [], [], []], "6": [[], [], [], []],
                 "7": [[], [], [], []], "8": [[], [], [], []], "9": [[], [], [], []], "10": [[], [], [], []], "11": [[], [], [], []], "12": [[], [], [], []]}
    
    # Number of months in a list
    months = np.arange(1, 13)

    # Lists for plotting
    avgTemp = []
    maxTemp = []
    minTemp = []
    avgPrecipitation = []

    # Do getting
    for day in weather:
        day = day.split(",")
        date = day[0].split("/")

        # Get data for plots 1-3
        if day[3] != '' and day[2] != '' and day[4] != '':
            # plt.plot(x, int(day[3]), c = 'r', linewidth = 1, label = 'Avg Wet Bulb Temp')
            avgWetBulbTemp.append(int(day[3]))
            avgPressure.append(float(day[2]))
            avgWindSpeed.append(float(day[4]))
            avgRelativeHumidity.append(float(day[6]))
            avgDewPoint.append(float(day[1]))

            x.append(i)
            i += 1

        # Getting data for plot 4
        if date[0] in monthDicData and day[7] != '' and day[8] != '' and day[9] != '' and day[5] != '':
            monthDicData[date[0]][0].append(float(day[7]))
            monthDicData[date[0]][1].append(float(day[8]))
            monthDicData[date[0]][2].append(float(day[9]))
            monthDicData[date[0]][3].append(float(day[5]))

    # Get averages, max, and min for each month
    for i in range (1,13):
        avgTemp.append(sum(monthDicData[str(i)][0]) / len(monthDicData[str(i)][0]))
        maxTemp.append(max(monthDicData[str(i)][1]))
        minTemp.append(min(monthDicData[str(i)][2]))
        avgPrecipitation.append(sum(monthDicData[str(i)][3]) / 10)

    # Plot 1
    # 2 graphs 1 plot or vise versa idk the correct terminology here
    fig, ax1 = plt.subplots()

    # Plot the average wet bulb temp
    ax1.plot(x, avgWetBulbTemp, c = 'r', label = 'Avg Wet Bulb Temp')
    ax1.set_xlabel("date")
    ax1.set_ylabel("Average Wet Bulb Temperature, F")

    # Make a second y axis
    # Plot the average pressure
    ax2 = ax1.twinx()
    ax2.plot(x, avgPressure, c = 'b', label = 'Avg Pressure')
    ax2.set_ylabel("Average Pressure, in Hg", fontsize=12)

    # Make a combined legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc="lower left")
    plt.title("Average Wet Bulb Temperature and Average Pressure")
    plt.show()

    # Plot 2
    plt.figure()

    # Make histogram of average wind speed
    # Bins are slightly different so not exactly like in the example
    plt.hist(avgWindSpeed, bins = 30, color='green', edgecolor='black', alpha=0.8)

    plt.title("Histogram of Average Wind Speed")
    plt.xlabel("Average Wind Speed, mph")
    plt.ylabel("Number of days")

    plt.show()

    # Plot 3
    plt.figure()

    # Make a scatterplot with average dew point on the x axis and average relative humidity on the y axis
    plt.scatter(avgDewPoint, avgRelativeHumidity, c = 'black', s = 10)

    plt.title("Average Relative Humidity vs Average Dew Point")
    plt.xlabel("Average Dew Point (F)")
    plt.ylabel("Average Relative Humidity (%)")

    plt.show()

    # Plot 4
    plt.figure()

    # Make a bar graph for average temperature of each month
    plt.bar(months, avgTemp, color = 'y')

    # Add lines onto that bar graph for the maximum temperature, minimum temperature, and average precipitation of each month
    plt.plot(months, maxTemp, c = 'r', label = 'High T')
    plt.plot(months, minTemp, c= 'b', label = 'Low T')
    plt.plot(months, avgPrecipitation, c = 'g', label = 'Precip')

    plt.title("Temperature and Precipitation by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature, F \nMonthly Precipitation, in")

    plt.legend()
    plt.show()
