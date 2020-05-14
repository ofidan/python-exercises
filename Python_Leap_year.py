year = int(input("enter a year: "))
if year % 4 == 0 and year % 400 == 0:
    print("{} is a leap year".format(year))
elif year % 100 == 0:
    print("{} is not a leap year".format(year))
elif year % 4 == 0:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))