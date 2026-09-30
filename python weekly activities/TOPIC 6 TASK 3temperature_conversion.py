# Temperature Conversion
# This program converts Celsius temperature to Fahrenheit.

# Define the conversion function
def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Get temperature from the user
celsius = float(input("Enter temperature in Celsius: "))

# Call the function
fahrenheit = convert_temperature(celsius)

# Display the result
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
