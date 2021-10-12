# Author JRI 10/12/21

p = int(input("Enter the amount of the principle investment "))
r = input("Enter the annual interest rate (as a decimal) ")
t = int(input("How many years is the money left in the account? "))

a = p * (1 + ((float(r) / 12) ** (12 * t)))
print(a)
