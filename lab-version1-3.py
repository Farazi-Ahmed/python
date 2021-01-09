# Question 6 Draw the flowchart of a program that reads two numbers from the user. Your program should then print “first is greater” if the first number is greater, “second is greater” if the second number is greater, and “the numbers are equal” otherwise.

a = int(input("First Number: "))
b = int(input("Second Number: "))

if a>b:
  print("first")
elif b>a:
  print("second")
else:
  print("numbers are equal")