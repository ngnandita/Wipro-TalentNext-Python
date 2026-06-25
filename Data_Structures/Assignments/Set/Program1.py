my_set = {10, 20, 30, 40, 50}

item = int(input("Enter item to remove: "))

if item in my_set:
    my_set.remove(item)
    print("Updated Set:", my_set)
else:
    print("Item not found in set")