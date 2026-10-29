# Transport System
# This program demonstrates inheritance using vehicles.

# Parent class
class Vehicle:

    def setVehicleDetails(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    def displayVehicle(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)


# Child class
class Bus(Vehicle):

    def setCapacity(self, capacity):
        self.capacity = capacity

    def displayBus(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)
        print("Passenger Capacity:", self.capacity)


# Main section
bus = Bus()

# Assign vehicle details
bus.setVehicleDetails("KDA 123A", "Isuzu")

# Assign passenger capacity
bus.setCapacity(50)

# Display bus information
print("--- Bus Details ---")
bus.displayBus()
