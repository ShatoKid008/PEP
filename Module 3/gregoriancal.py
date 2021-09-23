# leap year and common year calculator, which outputs results or if year isn't on Gregorian calendar


year = int(input("Enter a year: "))  # user input for the year
if year < 1582:  # if user input is before 1582 when Gregorian calendar began
    print("Not within the Gregorian calendar period.")  # print this
elif ((year % 4) == 0) == False:  # otherwise if this calculation is false
    year = "Common year"  # it means user input is a common year
elif ((year % 100) == 0) == False:  # otherwise if this calculation is false
    year = "Leap year"  # it means user input is a leap year
elif ((year % 400) == 0) == False:  # otherwise if this calculation is false
    year = "Common year"  # it means user input is a common year
else:
    year = "Leap year"  # otherwise it's a leap year
print(year)  # print the year

# You can also substitute this equation ((year%<xxx>)!=0) to the same effect
