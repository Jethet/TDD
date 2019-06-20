def leap_year(year):
    if year % 3 == 0:
        return False
    elif year % 4 == 0 and year % 100:
        return False
