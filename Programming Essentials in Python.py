# Module 1

# print ("Hisssss...")

# print("I like 'Monty Python'")

# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")


# Module 2 of PEP


# multiply a Monthy Python string by user's input
# x = input("how many MPs? (number): ")
# print("My name is Monty Python." * int(x))



# input calculator to display intergers to the power of 2
# anything = int(input("Enter a number: "))
# something = (anything) ** 2.0
# print(anything, "to the power of 2 is", something)



# calculating the end time (00:00) of a period of time 
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# mins = mins + dura # total time elapsed in minutes
# hour = hour + (mins // 60) # total hours elapsed
# mins = mins % 60 # remaining mins elapsed

# print(hour, mins, sep=":") # print in 00:00 format



# Module 3

# program using conditional execution to take user input on a plant name & output decision string
# PLily = input("What flower do we love?: ") # user input answer
# if PLily == "Spathiphyllum": # if user input is the same as correct answer
#     print("Yes - Spathiphyllum is the best plant ever!") # print specific string
# elif PLily == "spathiphyllum": # else if user input is this
#     print("No! I want a Big Spathiphyllum!") # print this specific string
# else: # if all previous conditions aren't met
#     print("It's Spathiphyllum! Not ",PLily,"!",sep='') # print "it's not" user input



# a tax calculator with conditions for processing amounts
# income = float(input("Enter the annual income: ")) # user inputs their salary to calculate their tax
# taxthresh = 85528 # tax threshold variable set

# if income < taxthresh: # if income is under threshhold
#     tax = (income * 0.18) - 556.02 # charge lower tax rate
# else:
#     tax = (0.32*(income - taxthresh)) + 14839.02 # otherwise charge higher tax rate

# if tax > 0: # if tax calculated above is greater than 0
#     tax = round(tax,0) # round the figure to the nearest unit
# else: # otherwise
#     tax=0.0 # the tax is 0.0
# print("The tax is:", tax, "thalers")



# leap year and common year calculator, which outputs results or if year isn't on Gregorian calendar
# year = int(input("Enter a year: ")) # user input for the year
# if year < 1582: # if user input is before 1582 when Gregorian calendar began
#     print("Not within the Gregorian calendar period.") # print this
# elif ((year%4)==0)== False: # otherwise if this calculation is false
#     year = "Common year" # it means user input is a common year
# elif ((year%100)==0)== False: # otherwise if this calculation is false
#     year = "Leap year" # it means user input is a leap year
# elif ((year%400)==0)== False: # otherwise if this calculation is false
#     year = "Common year" # it means user input is a common year
# else: year = "Leap year" # otherwise it's a leap year
# print(year) # print the year

# You can also substitute this equation ((year%<xxx>)!=0) to the same effect



# a guess the secret number game that traps user in a loop until they input the right integer
# secret_number = 777 # assigning the secret number into a variable

# print( # printing the welcome message to the game to the console
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# guess = int(input("Enter your guess to escape my loop, muggle!: ")) # user inputs their guess
# while guess != secret_number: # while the guess isn't equivalent to the secret number
#     if guess != secret_number: # if the the guess ins't equivalent to the secret number
#         print("Ha ha! You're stuck in my loop!") # print this message
#     guess = int(input("Enter your guess to escape my loop, muggle!: ")) # user has to try again and input another guess
#     
# if guess == secret_number: # if the user inputs a guess equivalent to the secret number # this also ends the while loop
#     print("Well done, muggle! You are free now.") # print this message

for i in range(2, 8):
    print("The value of i is currently", i)

