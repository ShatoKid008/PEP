# program using conditional execution to take user input on a plant name & output decision string


PLily = input("What flower do we love?: ")  # user input answer
if PLily == "Spathiphyllum":  # if user input is the same as correct answer
    print("Yes - Spathiphyllum is the best plant ever!")  # print specific string
elif PLily == "spathiphyllum":  # else if user input is this
    print("No! I want a Big Spathiphyllum!")  # print this specific string
else:  # if all previous conditions aren't met
    print("It's Spathiphyllum! Not ", PLily, "!", sep='')  # print "it's not" user input
