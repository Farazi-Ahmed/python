# Question 7 Draw the flowchart of a program that asks the user for a quantity, then takes that many numbers and prints the maximum, minimum and average of those numbers.

c=1
z = int(input("Limit? "))
sum = 0
max = -float('inf')
min = float('inf')

while c<=z:
  a = int(input("Next Number? "))
  if a>=max:
    max = a
  elif a<=min:
    min=a
  sum+=a
  c+=1
Average = sum/z
print(max, min, Average)