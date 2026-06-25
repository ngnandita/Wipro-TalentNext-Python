dictionary = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

key = int(input("Enter key to search: "))

if key in dictionary:
    print("Key exists")
else:
    print("Key does not exist")