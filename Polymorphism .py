# Base class representing a Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
