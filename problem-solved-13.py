# Question 13 : Take value of a, b, c, d from the user. Then print in such a way that

a=int(input("Value of a: "))
b=int(input("Value of b: "))
c=int(input("Value of c: "))
d=int(input("Value of d: "))
print (a)   
print (b)
print (c)
print (d)

# value of d goes to c 
# value of c goes to b
# value of b goes to a
# value of a goes to d

t1 = b
b = c
c = d
d = a
a = t1

print (a)
print (b)
print (c)
print (d)