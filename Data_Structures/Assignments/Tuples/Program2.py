# Write a program to check whether an element exists in a tuple or not.

numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in numbers:
    print("Element exists in tuple")
else:
    print("Element does not exist")