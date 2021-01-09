# Question 11 Prime Numbers between 40 and 50

a = 40
while a<=50:
  c=1
  d=0
  while c<=a:
    if a%c==0:
      d+=1
    c+=1
  if d==2:
    print("Prime number: "+str(a))
  a+=1