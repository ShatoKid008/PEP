# write and test a function which takes one argument (a year) and returns True
# if the year is a leap year, or False otherwise.


def is_year_leap(year):
    year = int(input("Enter a year: "))
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


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# write and test a function which takes two arguments (a year and a month)
# and returns the number of days for the given month/year pair
# (while only February is sensitive to the year value,
# your function should be universal).

def days_in_month(year, month):
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    numcal1 = [1, 3, 5, 7, 8, 10, 12]
    numcal2 = [2, 4, 6, 9, 11]

    if month in numcal1 and numcal2:
        if month in numcal1:
            return 31
        if month in numcal2:
            if month == 2:
                if year == is_year_leap(year):
                    return 29
                else:
                    return 28
            else:
                return 30
        else:
            return None


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# write and test a function which takes
# three arguments (a year, a month, and a day of the month)
# and returns the corresponding day of the year,
# or returns None if any of the arguments is invalid.
