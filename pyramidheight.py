# program to read inputted number of blocks and calculate height of pyramid that can be made
# each lower layer of the pyramid contains one block more than the layer above

blocks = int(input("Enter the number of blocks: "))
height = 0
layers = 1

while layers <= blocks:
    height += 1
    blocks -= layers
    layers += 1

print("The height of the pyramid:", height)