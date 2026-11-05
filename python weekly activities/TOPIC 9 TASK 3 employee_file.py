# Employee File Exception Handling
# This program reads employee information safely.

try:
    # Open the employee file
    f = open("employees.txt", "r")

    # Read and display the contents
    contents = f.read()
    print(contents)

    # Close the file
    f.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
