print("===================================")
print("      TRAVEL SUGGESTION SYSTEM")
print("===================================")

distance = float(input("Enter distance in miles: "))

if distance < 3:
    vehicle = "Bicycle"
elif distance < 300:
    vehicle = "Motor-Cycle"
else:
    vehicle = "Super-Car"

print("\nDistance:", distance, "miles")
print("Suggested Vehicle:", vehicle)
print("\nThank you for using Travel Suggestion System!")