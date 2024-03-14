# CHECK LEAP YEAR OR NOT

year = 2023

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a LEAP YEAR")
else:
    print(year, "is not a leap year")