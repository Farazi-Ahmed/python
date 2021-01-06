# Question 2: Draw the flowchart of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. 
# The mark ranges and corresponding grades are shown in the table below. Valid range of marks is 0 to 100. Print “Wrong Input” otherwise.
# Marks: Grade
# 90 and above : A
# 80-89 : B
# 70-79 : C
# 60-69 : D
# 50-59 : E
# Below 50 : F


a=int(input("Provide your mark: "))

if a<0 or a>100:
  print("Wrong Input")
elif a>=90:
  print("A")
elif a>=80:
  print("B")
elif a>=70:
  print("C")
elif a>=60:
  print("D")
elif a>=50:
  print("E")
else:
  print("Fail")