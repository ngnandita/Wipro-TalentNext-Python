from collections import Counter

filename = input("Enter filename: ")

try:
    with open(filename, 'r') as file:
        words = []

        for line in file:
            words.extend(line.split())

        total_lines = len(open(filename).readlines())

        if total_lines > 12:
            meeting_time = total_lines - 12
            print("Meeting Time:", meeting_time, "PM")
        else:
            print("Meeting Time:", total_lines, "AM")

        count = Counter(words)

        place = count.most_common(1)[0][0]

        print("Meeting Place:", place + " Street")

except FileNotFoundError:
    print("File not found")