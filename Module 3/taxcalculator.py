# a tax calculator with conditions for processing amounts


income = float(input("Enter the annual income: "))  # user inputs their salary to calculate their tax
taxthresh = 85528  # tax threshold variable set

if income < taxthresh:  # if income is under threshold
    tax = (income * 0.18) - 556.02  # charge lower tax rate
else:
    tax = (0.32 * (income - taxthresh)) + 14839.02  # otherwise charge higher tax rate

if tax > 0:  # if tax calculated above is greater than 0
    tax = round(tax, 0)  # round the figure to the nearest unit
else:  # otherwise
    tax = 0.0  # the tax is 0.0
print("The tax is:", tax, "thalers")
