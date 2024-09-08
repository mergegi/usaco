def isLeapYear(year): # year is the number for the year, e.g, 2024, 1990
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
         return True
    return False

print(isLeapYear(1900))    