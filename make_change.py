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
# Date: 11 09 2025
#

paid = float(str((input("How much did you pay? "))))
cost = float(str((input("How much did it cost? "))))

r = paid - cost # some number less than 1, remainder in dollars
print(f"You received ${r:.2f} in change. That is ...")
r *= 100 # convert to cents
r = int(round(r, 1))
q = r // 25
r -= q * 25
d = r // 10
r -=d*10
n = r // 5
r-=5*n
p = r

if q != 0 and q != 1:
    print(f"{q} quarters")
elif q == 1:
    print(f"{q} quarter")

if d != 0 and d != 1:
    print(f"{d} dimes")
elif d == 1:
    print(f"{d} dime")

if n != 0 and n != 1:
    print(f"{n} nickels")
elif n == 1:
    print(f"{n} nickel")

if p != 0 and p != 1:
    print(f"{p} pennies")
elif p == 1:
    print(f"{p} penny")
