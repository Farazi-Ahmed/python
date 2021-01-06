# Question 6 : calculate the values of L for different values of S

S=int(input("Value of S: "))

if S<100:
  L = 3000 - (125 * S * S)
else:
  L = 12000 / (4 + ((S * S)/14900))

print(L)