# Question 9 Perfect Number

a = int(input("Number? "))
c=1
d=0
while c<a:
  if a%c==0:
    d+=c
  c+=1
if d==a:
  print("Perfect")
else:
  print("Not Perfect")