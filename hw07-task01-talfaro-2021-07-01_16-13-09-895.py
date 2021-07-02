# Task01 - Create a vehicle class that makes use of encapsulation with the correct naming
# conventions. It should contain the following:
# - Accessors: wheels, doors, fuel, temperature
# - Mutators: fuel
# car.get_wheels()                                  4
# car.get_wheels(100)


class Car:

    def __init__(self, wheels, doors, fuel, temperature):
        self.wheels = wheels
        self.doors = doors
        self.fuel = fuel
        self.temperature = temperature

    def get_doors(self, doors):
        self.doors = doors
        print("This car has ", self.doors," doors.")


    def get_wheels(self, wheels):
        self.wheels = wheels
        return wheels


    def get_temp(self, temperature):
        self.temperature = temperature
        return temperature

    def get_fuel(self, fuel):
        self.fuel = fuel
        return fuel


    def set_fuel(self, fuel):
        self.fuel = fuel
        return fuel

Vehicle1 = Car(wheels,doors,fuel,temperature)
print(Vehicle1)
