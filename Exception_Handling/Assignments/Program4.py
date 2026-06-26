numbers = [10, -5, 20, -8, 15, -30, 50, -60, 80, -100]

try:
    index = int(input("Enter index (0-9): "))

    if numbers[index] >= 0:
        print(numbers[index], "is Positive")
    else:
        print(numbers[index], "is Negative")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer.")