# program to remove repeated numbers from a user inputed list


my_list = []
new_list = []
list_size = int(input("How many numbers are in your list?: "))

for i in range(list_size):
    entry = int(input("Enter numbers: "))
    my_list.append(entry)

for number in my_list:
    if number not in new_list:
        new_list.append(number)

my_list = new_list[:]

print("The list with unique elements only:")
print(my_list)
