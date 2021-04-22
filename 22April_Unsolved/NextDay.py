def isLeapYear(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    return False

date = input()
day, month, year = date.split(":")
day, month, year = int(day), int(month), int(year)
day_30 = [4, 6, 9, 11]
if month in day_30:
    month_length = 30
elif month == 2:
    if isLeapYear(year):
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 31

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("Next Date is:",str(day)+":"+str(month)+":"+str(year))
