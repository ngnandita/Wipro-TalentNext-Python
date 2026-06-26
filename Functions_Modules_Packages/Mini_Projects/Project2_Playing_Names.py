"""
Module : name_utils
"""

def ispalindrome(name):
    if name.lower() == name.lower()[::-1]:
        return "Yes it is a palindrome."
    return "No! It is not a palindrome."


def count_the_vowels(name):
    vowels = "aeiou"
    count = 0

    for ch in name.lower():
        if ch in vowels:
            count += 1

    return count


def frequency_of_letters(name):
    frequency = {}

    for ch in name.lower():
        if ch != " ":
            frequency[ch] = frequency.get(ch, 0) + 1

    return frequency