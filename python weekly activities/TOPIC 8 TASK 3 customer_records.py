# Reading Customer Records
# This program reads and displays information from customers.txt.

# Open the file in read mode
f = open("customers.txt", "r")

# Read the contents
contents = f.read()

# Display the contents
print(contents)

# Close the file
f.close()
