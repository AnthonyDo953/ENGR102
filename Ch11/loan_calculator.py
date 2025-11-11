# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 11.16.1 Loan Calculator
# Date: 10 November 2025

outfile = open(input("Enter the output filename: "), 'w')
P = int(input("Enter the principal amount: "))
N = int(input("Enter the term length (months): "))
i = float(input("Enter the annual interest rate: "))

loanBalance = P
totalInterest = 0

M = (P * i / 12) / (1 - (1 / (1 + i / 12)) ** N)

outfile.write("Month,Total Accrued Interest,Loan Balance\n")

# Write to file
for j in range(N + 1):
    if loanBalance > 0:
        outfile.write(f"{j},${totalInterest:.2f},${loanBalance:.2f}\n")
        monthlyInterest = loanBalance * i / 12
        totalInterest += monthlyInterest
        loanBalance = loanBalance + monthlyInterest - M
    else: 
        outfile.write(f"{j},${totalInterest:.2f},${0.00}")
