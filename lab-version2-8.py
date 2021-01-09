# Question 10 Prime Number
a = int(input("Enter Number: "))
c=1
d=0
while c<=a:
  if a%c==0:
    d+=1
  c+=1
if d==2:
  print("Prime")
else:
  print("Not Prime")