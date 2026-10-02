# Create empty list
names = []

# Prompt user - using input() and append()
print("Enter names one by one. Press ENTER with no name to stop.")
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    names.append(name)  # add to list

# Count total entered
total_entered = len(names)
print(f"\nTotal number of names entered: {total_entered}")

# Remove duplicates using set() and convert back to list
unique_names = list(set(names))

# Sort in alphabetical order using sort()
unique_names.sort()

# Display final list using print()
print("Final sorted list without duplicates:")
print(unique_names)
