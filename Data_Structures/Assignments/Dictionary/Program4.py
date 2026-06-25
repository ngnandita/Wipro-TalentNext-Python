dictionary = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

print("Keys:")
for key in dictionary:
    print(key)

print("\nValues:")
for value in dictionary.values():
    print(value)

print("\nKeys and Values:")
for key, value in dictionary.items():
    print(key, ":", value)