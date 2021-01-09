# Question 3 Draw the flowchart of a program that reads the radius of a circle and prints its circumference and area.

import math

radius = int(input("Provide your radius: "))
pi = math.pi
circumference = 2 * pi * radius
area = pi * radius * radius

# formatter style (decimal places is the number)
print("%.3f"%area)

print(circumference, area)