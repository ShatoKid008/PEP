# a guess the secret number game that traps user in a loop until they input the right integer


secret_number = 777  # assigning the secret number into a variable
print(  # printing the welcome message to the game to the console
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter your guess to escape my loop, muggle!: "))  # user inputs their guess
while guess != secret_number:  # while the guess isn't equivalent to the secret number
    if guess != secret_number:  # if the the guess isn't equivalent to the secret number
        print("Ha ha! You're stuck in my loop!")  # print this message
    guess = int(input("Enter your guess to escape my loop, muggle!: "))  # user has to try again and input another guess

if guess == secret_number:  # if the user inputs a guess equivalent to the secret number # this also ends the while loop
    print("Well done, muggle! You are free now.")  # print this message
