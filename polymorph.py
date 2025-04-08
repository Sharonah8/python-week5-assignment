# a base class with a generic move method
class Vehicle:
    def move(self):
        print("The vehicle moves")

#vehicle subclasses with different move versions
class Car(Vehicle):
    def move(self):
        print("Drives on the road")

class Plane(Vehicle):
    def move(self):
        print("Flies in the sky")
    
class Boat(Vehicle):
    def move(self):
        print("Sails on water")
    
#creating a list of vehicles
vehicles = [Car(), Plane(), Boat()]

#looping through each vehicle and calling the move method
for vehicle in vehicles:
    vehicle.move()