# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: 4.16 Lab: Make Change
# Date: 12 09 2025
#

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

dA = str(A)
dB = str(B)
dC = str(C)

# Fuck you bitch
if A == 0:
    dA  = ""
elif A == 1:
    dA = "x^2"
elif A == -1:
    dA = "- x^2"
elif A < 0:
    dA = " ".join(dA)
    dA = dA + "x^2"
else:
    dA = dA + "x^2"

if B == 0:
    dB = ""
elif B == 1 and A != 0:
    dB = "+ x"
elif B == 1:
    dB = "x"
elif B == -1:
    dB = "- x"
elif B < 0:
    dB = " ".join(dB) + "x"
elif B > 0 and A == 0:
    dB = dB + "x"
else:
    dB = "+ " + dB + "x"

if C == 0:
    dC = ""
elif C == 1 and A != 0 and B != 0:
    dC = "+ " + dC
elif C < 0:
    dC = " ".join(dC)
else:
    dC = "+ " + dC

prettyEquation = f"The quadratic equation is {dA} {dB} {dC} = 0"

if dA == "":
    prettyEquation = f"The quadratic equation is {dB} {dC} = 0"
    if dB == "":
        prettyEquation = f"The quadratic equation is {dC} = 0"
elif dB == "":
    prettyEquation = f"The quadratic equation is {dA} {dC} = 0"
    if dC == "":
        prettyEquation = f"The quadratic equation is {dA} = 0"
elif dC == "":
    prettyEquation = f"The quadratic equation is {dA} {dB} = 0"
    if dA == "":
        prettyEquation = f"The quadratic equation is {dB} = 0"

print(prettyEquation)
