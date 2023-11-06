def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def months(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    return months_days[month - 1]


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
check_days_in_year = months(year, month)
print(check_days_in_year)
