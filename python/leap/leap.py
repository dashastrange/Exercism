def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0 or year % 3 == 0:
        return False
    return year % 4 == 0
