# Question 8 Draw the flowchart of a program that takes a number from user and prints the divisors of that number and then how many divisors there were.

a=int(input("Number? "))
c=1
d=0
while c<=a:
  if a%c==0:
    d+=1  
    print(c)
  c+=1
print("Divisors in total: "+str(d))