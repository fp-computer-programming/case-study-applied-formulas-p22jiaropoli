# Author JRI 10/12/21

x1 = int(input("Enter the first x value "))
x2 = int(input("Enter the second x value "))
y1 = int(input("Enter the first y value "))
y2 = int(input("Enter the second y value "))

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
print(distance)
