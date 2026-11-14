# Transport Fare System
# This program demonstrates polymorphism.

# Parent class
class Vehicle:

    def calculateFare(self, distance):
        pass


# Bus class
class Bus(Vehicle):

    def calculateFare(self, distance):
        return distance * 50


# Taxi class
class Taxi(Vehicle):

    def calculateFare(self, distance):
        return distance * 100


# Main section
bus = Bus()
taxi = Taxi()

# Distance travelled
distance = 10

# Calculate fares
bus_fare = bus.calculateFare(distance)
taxi_fare = taxi.calculateFare(distance)

# Display results
print("--- Transport Fares ---")
print(f"Bus Fare: KSh {bus_fare}")
print(f"Taxi Fare: KSh {taxi_fare}")
