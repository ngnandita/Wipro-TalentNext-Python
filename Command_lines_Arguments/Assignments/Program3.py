import sys

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

total = 0

for value in sys.argv[1:]:
    number = int(value)
    if is_prime(number):
        total += number

print("Sum of Prime Numbers =", total)