# Module 1 of PEP

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
#     if guess != secret_number: # if the the guess isn't equivalent to the secret number
#         print("Ha ha! You're stuck in my loop!") # print this message
#     guess = int(input("Enter your guess to escape my loop, muggle!: ")) # user has to try again and input another guess
#     
# if guess == secret_number: # if the user inputs a guess equivalent to the secret number # this also ends the while loop
#     print("Well done, muggle! You are free now.") # print this message



# A for loop program to count "mississippily" to five using the time module.
# import time # For timed output to the console.
#
# for count in range(1, 6): # A for loop that counts to five.
#     print(count,"Mississippi") # print the loop iteration number and the word "Mississippi".
#     time.sleep(1) # use: time.sleep(1) to time output to console to 1 second
#
# print("Ready or not, here I come!") # print the final message.



# A program that uses a while loop and continuously asks user to enter a word until the secret exit word is entered
# secret_exit_word = "chupacabra" # defining the secret exit word
# guess = input("Can you guess the secret exit word to escape the loop?: ") # user inputs guess
#
# while guess != secret_exit_word: # while guess is incorrect
#     guess = input("Incorrect. Guess again!: ") # user gets incorrcet message and guesses again
#     if guess == secret_exit_word: # if user guesses correctly
#         break # break
#
# print("You've successfully left the loop.") # print success message

# the ugly vowel eater game
# user inputs a word and program prints the word vertically, without the vowels
# user_word = input("Enter a word and watch it's vowels disappear!: ") # Prompt the user to enter a word
# user_word = user_word.upper()# and assign it to the user_word variable.
# vowel_eaten_word = ""
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         vowel_eaten_word += letter
#
# for i in vowel_eaten_word:
#     print(i)



# program to read inputted number of blocks and calculate height of pyramid that can be made
# each lower layer of the pyramid contains one block more than the layer above
# blocks = int(input("Enter the number of blocks: "))
# height = 0
# layers = 1
#
# while layers <= blocks:
#     height += 1
#     blocks -= layers
#     layers += 1
#
# print("The height of the pyramid:", height)



# program to test Collatz' hypothesis against user input
# program reads one natural number and executes below step as long as c0 is different from 1
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# c0 = int(input("Enter a number: "))
# steps = 0
#
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 /= 2
#     elif c0 % 2 == 1:
#         c0 = 3 * c0 + 1
#     steps += 1
#     print(int(c0))
#
# print("steps =", steps)



# # program to manipulate indexed items in a list
# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# print("\n",hat_list)
# guess = int(input("Replace the middle number with: ")) # Step 1: write a line of code that prompts the user
# hat_list[2] = guess # to replace the middle number with an integer number entered by the user.
# print(hat_list)
# del hat_list[-1]# Step 2: write a line of code that removes the last element from the list.
# print(hat_list)
# print(len(hat_list))# Step 3: write a line of code that prints the length of the existing list.
#
# print(hat_list)



