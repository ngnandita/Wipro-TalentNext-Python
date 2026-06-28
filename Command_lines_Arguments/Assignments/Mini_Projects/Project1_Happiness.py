import sys

string1 = sys.argv[1].split('-')
string2 = sys.argv[2].split('-')
string3 = sys.argv[3].split('-')

happiness = 0

for num in string3:
    if num in string1:
        happiness += 1
    elif num in string2:
        happiness -= 1

print("Final happiness:", happiness)

