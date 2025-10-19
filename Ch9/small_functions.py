# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 9.20.1 Small Functions
# Date: 23 October 2025

from math import *

def parta(numbers):
    numbersSorted = sorted(numbers)
    output = [numbersSorted[0], numbersSorted[len(numbersSorted) - 1]]
    if len(numbersSorted) % 2 == 0:
        output.insert(1, (numbersSorted[int(len(numbersSorted) / 2)] + numbersSorted[int(len(numbersSorted) / 2 - 1)]) / 2)
    else:
        output.insert(1, numbersSorted[int(len(numbersSorted) / 2)])
    return output

def partb(times, distances):
    output = []
    for i in range(1, len(times)):
        output.append((distances[i] - distances[i-1]) / (times[i] - times[i-1]))
    return output

def partc(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == 2029:
                return numbers[i] * numbers[j]
    return False

def partd(n):
    total = 0
    sumList = []
    i = 0
    while i <= n:
        if total == n:
            return sumList
        elif total < n:
            sumList.append(i)
            total = sum(sumList)
        else:
            while total > n:
                del sumList[0]
                total = sum(sumList)
            i -= 2
        i += 2
    return False

def parte(rSphere, rHole):
    h = sqrt(rSphere ** 2 - rHole ** 2)
    return round((4 / 3) * pi * h ** 3, 6)

def partf(char, name, company, email):
    info = [name, company, email]
    longest = max([len(name), len(company), len(email)])
    businessCard = ""
    businessCard += ''.join([char for i in range(longest + 6)]) + "\n"
    for thing in info:
        businessCard += char + thing.center(longest + 4) + char + "\n"
    businessCard += ''.join([char for i in range(longest + 6)]) + "\n"
    return businessCard

def partg(x, tolerance):
    summation = 0
    n = 1
    while True:
        term = 2 / (2 * n -1) * x ** (2 * n - 1)

        if abs(term) < tolerance:
            break

        summation += term
        n += 1

    return summation
