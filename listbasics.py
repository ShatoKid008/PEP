# the basics of lists lab


beatles = []  # step 1  create an empty list named beatles
print("Step 1:", beatles)

beatles.append(
    "John Lennon")  # step 2 use the append() method to add the following members of the band to the list: John
# Lennon, Paul McCartney, and George Harrison
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(0,
               2):  # step 3 use the for loop and the append() method to prompt the user to add the following members
    # of the band to the list: Stu Sutcliffe, and Pete Best
    beatles.append(input("Enter a beatle: "))
    continue
print("Step 3:", beatles)

del beatles[-1]  # step 4 use the del instruction to remove Stu Sutcliffe and Pete Best from the list
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")  # step 5 use the insert() method to add Ringo Starr to the beginning of the list
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))
