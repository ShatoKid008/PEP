# A for loop program to count "mississippily" to five using the time module.

import time  # Will use sleep function from this module for timed output to the console.

for count in range(1, 6):  # A for loop that counts to five.
    print(count, "Mississippi")  # print the loop iteration number and the word "Mississippi".
    time.sleep(1)  # use: time.sleep(1) to time output to console to 1 second

print("Ready or not, here I come!")  # print the final message.
