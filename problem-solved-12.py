# Question 12 : Take value of a, b, c from the user. Then print in such a way that
# value of a goes to b
# value of b goes to c
# value of c goes to a

x=int(input("Value of x: "))
y=int(input("Value of y: "))
z=int(input("Value of z: "))
#print (x)              
#print (y) 
#print (z)

t1 = z
z = y
y = x
x = t1

print (x)
print (y)
print (z)