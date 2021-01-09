# Question 4 Draw flowchart of a program, which adds all numbers that are multiples of either 7 or 9 but not both, up to 600. 

a = 1
sum = 0

while a<=600:
  if (a%7!=0 and a%9==0) or (a%7==0 and a%9!=0):
    sum+=a
  a+=1
print(sum)