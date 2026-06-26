word = input("Enter word to search: ")

file = open("sample.txt", "r")

content = file.read().lower()

count = content.split().count(word.lower())

print("Frequency =", count)

file.close()