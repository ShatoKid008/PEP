# program to test Collatz' hypothesis against user input
# program reads one natural number and executes below step as long as c0 is different from 1
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.

c0 = int(input("Enter a number: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
    steps += 1
    print(int(c0))

print("steps =", steps)
