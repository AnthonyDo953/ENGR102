# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 9.20.1 Small Functions
# Date: 23 October 2025

from math import * 

# parta: returns a tuple containing (minimum, median, maximum) from a list of numbers
def parta(numbers):
    numbersSorted = sorted(numbers)  # sort the list in ascending order
    # start output list with the smallest and largest values
    output = [numbersSorted[0], numbersSorted[len(numbersSorted) - 1]]
    
    # check if the number of elements is even
    if len(numbersSorted) % 2 == 0:
        # if even, median is the average of the two middle elements
        output.insert(1, (numbersSorted[int(len(numbersSorted) / 2)] + numbersSorted[int(len(numbersSorted) / 2 - 1)]) / 2)
    else:
        # if odd, median is the middle element
        output.insert(1, numbersSorted[int(len(numbersSorted) / 2)])
    
    # return a tuple (min, median, max)
    return (output[0], output[1], output[2])


# partb: calculates average speeds (or rates of change) between consecutive time points
def partb(times, distances):
    output = []
    # loop through each pair of consecutive points
    for i in range(1, len(times)):
        # slope formula: (change in distance) / (change in time)
        output.append((distances[i] - distances[i-1]) / (times[i] - times[i-1]))
    return output  # return list of calculated rates


# partc: finds two numbers in a list that sum to 2029, returns their product if found
def partc(numbers):
    # nested loops check all unique pairs
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == 2029:  # check if sum equals 2029
                return numbers[i] * numbers[j]     # return product of the pair
    return False  # return False if no matching pair found


# partd: finds a sequence of even numbers that add up exactly to n
def partd(n):
    total = 0          # running total of current sequence
    sumList = []       # list storing the current sequence
    i = 0              # start from 0 and go up by 2 (even numbers)
    
    while i <= n:      # continue while current number is less than or equal to n
        if total == n:
            return sumList  # if sum matches n, return the sequence
        elif total < n:
            # if total is less than n, add next even number
            sumList.append(i)
            total = sum(sumList)
        else:
            # if total exceeds n, remove numbers from start until total <= n
            while total > n:
                del sumList[0]
                total = sum(sumList)
            i -= 2  # adjust to recheck current even number
        i += 2  # increment by 2 to go to next even number
    
    return False  # return False if no such sequence is found


# parte: computes the volume of a sphere segment remaining after drilling a cylindrical hole
def parte(rSphere, rHole):
    # calculate the height of the spherical cap using Pythagorean theorem
    h = sqrt(rSphere ** 2 - rHole ** 2)
    # compute the volume of the remaining "band" and round to 6 decimal places
    return round((4 / 3) * pi * h ** 3, 6)


# partf: generates a formatted text "business card" using a border character
def partf(char, name, company, email):
    info = [name, company, email]  # info lines for the card
    # determine width based on the longest string
    longest = max([len(name), len(company), len(email)])
    businessCard = ""
    
    # create top border
    businessCard += ''.join([char for i in range(longest + 6)]) + "\n"
    
    # center each line of text inside the border
    for thing in info:
        businessCard += char + thing.center(longest + 4) + char + "\n"
    
    # create bottom border
    businessCard += ''.join([char for i in range(longest + 6)]) + "\n"
    return businessCard  # return the formatted card string


# partg: approximates a mathematical series until the term size is below a given tolerance
def partg(x, tolerance):
    summation = 0  # store total sum
    n = 1          # term index, starting at 1
    
    while True:
        # compute the next term in the series
        term = 2 / (2 * n - 1) * x ** (2 * n - 1)
        
        # stop if the term's magnitude is smaller than tolerance
        if abs(term) < tolerance:
            break
        
        summation += term  # add term to running total
        n += 1             # move to next term
    
    return summation  # return the final approximation
