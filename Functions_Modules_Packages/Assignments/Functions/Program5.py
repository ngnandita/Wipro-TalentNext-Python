def even_numbers(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    print("Even Numbers =", even)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(sample_list)