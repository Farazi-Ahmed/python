# Question 2 Draw flowchart of a program, which adds all numbers that are multiples of both 7 and 9 up to 600.

a = 1
sum = 0

while a<=600:
  if a%7==0:
    if a%9==0:
      sum+=a
  a+=1
print(sum) 