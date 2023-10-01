# write a program thyat determines wheather a year entered by the users is a leap year or not using.if-elif-else statement
#leap year
"""
year%4==0 &
year%100!=0 /
year%400==0
"""

year = 2022

if (year % 400 == 0 and year % 100 == 0):
  print("{0} is a leap year".format(year))
elif (year % 4 == 0 and year % 100 != 0):
  print("{0} is a leap year".format(year))
else:
  print("{0} is not a leap year".format(year))
