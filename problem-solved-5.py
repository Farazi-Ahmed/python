# Question 5: Write a flowchart that finds the number of hours, minutes, and seconds in a given number of seconds.

HowManySec = int(input("Input Seconds: "))

Hours= HowManySec // 3600
SecLeft= HowManySec % 3600
Minutes= SecLeft // 60
SecLeft= HowManySec % 60

print(str(Hours)+" hours",str(Minutes)+" mins",str(SecLeft)+" seconds")