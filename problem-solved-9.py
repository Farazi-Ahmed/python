# Question 9 : Draw flowchart of a program to find the largest among three different numbers entered by user.

x=int(input("Value of x: "))
y=int(input("Value of y: "))
z=int(input("Value of z: "))

if x>y and x>z:
  print(x)
elif y>z and y>x:
  print(y)
else:
  print(z)

MaxValue = max(x,y,z)

print(MaxValue)