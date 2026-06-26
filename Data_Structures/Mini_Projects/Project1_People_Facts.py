# Dictionary of people and their interesting facts


people = {
    "Jeff": "is afraid of Dogs.",
    "David": "plays the piano.",
    "Jason": "can fly an airplane."
}

print("===== Original List =====")
for name, fact in people.items():
    print(name + ":", fact)


people["Jeff"] = "is afraid of heights."


people["Jill"] = "can hula dance."


print("\n===== Updated List =====")
for name, fact in people.items():
    print(name + ":", fact)