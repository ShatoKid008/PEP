# A program that uses a while loop and continuously asks user to enter a word until the secret exit word is entered

secret_exit_word = "chupacabra"  # defining the secret exit word
guess = input("Can you guess the secret exit word to escape the loop?: ")  # user inputs guess

while guess != secret_exit_word:  # while guess is incorrect
    guess = input("Incorrect. Guess again!: ")  # user gets incorrcet message and guesses again
    if guess == secret_exit_word:  # if user guesses correctly
        break  # break

print("You've successfully left the loop.")  # print success message
