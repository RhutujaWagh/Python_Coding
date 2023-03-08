# Write a Python program which accepts the radius of a circle from the user and
# compute the area.
# Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi
r = float(input("Enter the redius:"))
print("Area:" + str(pi*r**2))