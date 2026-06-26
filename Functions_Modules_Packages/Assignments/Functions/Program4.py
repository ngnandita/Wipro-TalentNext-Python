def count_letters(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase Letters =", upper)
    print("Lowercase Letters =", lower)

string = input("Enter a string: ")

count_letters(string)