# the ugly vowel eater game
# user inputs a word and program prints the word vertically, without the vowels

user_word = input("Enter a word and watch it's vowels disappear!: ")  # Prompt the user to enter a word
user_word = user_word.upper()  # and assign it to the user_word variable.
vowel_eaten_word = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        vowel_eaten_word += letter

for i in vowel_eaten_word:
    print(i)
