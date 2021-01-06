# Question 7: Write a flowchart that reads the values for the three sides x, y, and z of a triangle, and then calculates its area.

x=int(input("Value of x: "))
y=int(input("Value of y: "))
z=int(input("Value of z: "))

s = (x + y + z) / 2

area = ((s * (s-x)*(s-y)*(s-z)) ** 0.5)

print(area)