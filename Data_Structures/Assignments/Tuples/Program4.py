#Write a program to find the index of an item in a tuple.

numbers = (10, 20, 30, 40, 50)

item = int(input("Enter item: "))

if item in numbers:
    print("Index =", numbers.index(item))
else:
    print("Item not found")