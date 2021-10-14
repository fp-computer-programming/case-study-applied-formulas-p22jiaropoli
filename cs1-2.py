# Author JRI 10/12/21

p = float(input("Enter the amount of the principle investment "))
r = float(input("Enter the annual interest rate (as a decimal) "))
t = float(input("How many years is the money left in the account? "))

a = p * ((1 + (r / 12)) ** (12 * t))
print(a)
