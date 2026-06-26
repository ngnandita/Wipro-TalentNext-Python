try:
    filename = input("Enter the file name: ")

    file = open(filename, 'r')

    total_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        if parts[0].lower() == "discount":
            discount = int(parts[1])

        elif parts[1].lower() == "free":
            total_items += 1
            free_items += 1

        else:
            total_items += 1
            amount += int(parts[1])

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", amount - discount)

    file.close()

except FileNotFoundError:
    print("File does not exist")

except Exception as e:
    print("Error:", e)

    not working