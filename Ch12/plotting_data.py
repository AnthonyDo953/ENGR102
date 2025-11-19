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

with open("WeatherDataCLL.csv", 'r') as weather:
    
    nextLine = weather.readline()
    nextLine = weather.readline()

    i = 1 

    x = []
    avgWetBulbTemp = []
    avgPressure = []
    avgWindSpeed = []
    avgRelativeHumidity = []
    avgDewPoint = []


    # Do getting
    for day in weather:
        day = day.split(",")
        date = day[0].split("/")

        if day[3] != '' and day[2] != '' and day[4] != '':
            # plt.plot(x, int(day[3]), c = 'r', linewidth = 1, label = 'Avg Wet Bulb Temp')
            avgWetBulbTemp.append(int(day[3]))
            avgPressure.append(float(day[2]))
            avgWindSpeed.append(float(day[4]))
            avgRelativeHumidity.append(float(day[6]))
            avgDewPoint.append(float(day[1]))

            x.append(i)
            i += 1

    # fig, ax1 = plt.subplots()

    # ax1.plot(x, avgWetBulbTemp, c = 'r', label = 'Avg Wet Bulb Temp')
    # ax1.set_xlabel("date")
    # ax1.set_ylabel("Average Wet Bulb Temperature, F")

    # ax2 = ax1.twinx()
    # ax2.plot(x, avgPressure, c = 'b', label = 'Avg Pressure')
    # ax2.set_ylabel("Average Pressure, in Hg", fontsize=12)

    # lines_1, labels_1 = ax1.get_legend_handles_labels()
    # lines_2, labels_2 = ax2.get_legend_handles_labels()
    # ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc="lower left")
    # plt.title("Average Wet Bulb Temperature and Average Pressure")
    # plt.show()

    # plt.figure()

    # plt.hist(avgWindSpeed, bins = 30, color='green', edgecolor='black', alpha=0.8)

    # plt.title("Histogram of Average Wind Speed")
    # plt.xlabel("Average Wind Speed, mph")
    # plt.ylabel("Number of days")

    # plt.show()

    plt.figure()

    plt.scatter(avgDewPoint, avgRelativeHumidity, c = 'black', s = 10)

    plt.title("Average Relative Humidity vs Average Dew Point")
    plt.xlabel("Average Dew Point (F)")
    plt.ylabel("Average Relative Humidity (%)")

    plt.show()


