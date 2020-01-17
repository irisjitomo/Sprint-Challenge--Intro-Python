# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass

class GroundVehicle(Vehicle):
    pass
    # super().__init__(#VehicleAttributes)

class FlightVehicle(Vehicle):
    pass
    # super().__init__(#VehicleAttributes)

class Starship(Flightvehicle):
    pass

class Car(GroundVehicle):
    pass # new subclass attributes
    # super().__init__(#GroundVehicleAttributes)

class Motorcycle(GroundVehicle):
    pass

class Airplane(FlightVehicle):
    pass


