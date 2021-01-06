# Question 15 : Take hour from the user as input and tell it is time for which meal.

hour=int(input("Place the time of hour here: "))

if hour>23 or hour<0:
  print("Invalid Time")
elif hour>=4 and hour<=6:
  print("Breakfast")
elif hour>=12 and hour<=13:
  print("Lunch")
elif hour>=16 and hour<=17:
  print("Snacks")
elif hour>=19 and hour<=20:
  print("Dinner")
else:
  print("Patience is a virtue")