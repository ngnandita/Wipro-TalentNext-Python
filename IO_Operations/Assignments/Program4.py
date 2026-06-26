file = open("sample.txt", "r")

lines = file.readlines()

result = []

for line in lines:
    result.append(line.strip())

print(result)

file.close()