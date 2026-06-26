try:
    number = int(input("Enter a number: "))

    if number < 2:
        print(number, "is not a Prime Number")

    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(number, "is not a Prime Number")
                break
        else:
            print(number, "is a Prime Number")

except ValueError:
    print("Error: Please enter a valid integer.")