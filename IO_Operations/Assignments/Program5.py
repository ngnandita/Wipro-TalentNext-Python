file = open("sample.txt", "r")

words = file.read().split()

longest = max(words, key=len)

print("Longest Word =", longest)

file.close()