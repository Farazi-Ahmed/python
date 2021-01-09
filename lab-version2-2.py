# Question 1d Loop: 18,-27,36,-45,54,-63
a = 18
c = 1

while c<=6:
  if c%2==0:
    print(a*-1,end=" ")
  else:
    print(a,end=" ")
  a+=9
  c+=1