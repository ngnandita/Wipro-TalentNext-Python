string = input("Enter a string: ")

if string.startswith('x'):
    string = string[1:]

if string.endswith('x'):
    string = string[:-1]

print(string)