# Question 4: Write a flowchart that calculates the tax as follows:
# a) No tax if you get paid less than 10,000
# b) 5% tax if you get paid between 10K and 20K
# c) 10% tax if you get paid more than 20K
# d) NO TAX IF YOU ARE LESS THAN 18 YEARS OLD.


PMT = int(input("Provide your salary: "))
Age = int(input("Provide your age: "))

if Age<18 or PMT <10000:
  tax = 0
elif PMT <20000:
  tax = 0.05
else:
  tax = 0.10

TotalTaxAmount = PMT * tax
print("Your Tax is $ "+str(TotalTaxAmount))