# Task01 - Create a vehicle class that makes use of encapsulation with the correct naming
# conventions. It should contain the following:
# - Accessors: wheels, doors, fuel, temperature
# - Mutators: fuel
# car.get_wheels()                                  4
# car.get_wheels(100)

import time

class Car:

    def __init__(self, wheels, doors, fuel, temperature):
        self.__wheels = wheels
        self.__doors = doors
        self.__fuel = fuel
        self.__temperature = temperature

    def set_doors(self, doors):
        self.__doors = doors
        return doors

    def get_doors(self):
        return self.__doors

    def set_wheels(self, wheels):
        self.__wheels = wheels
        return wheels

    def get_wheels(self):
        return self.__wheels

    def set_temp(self, temperature):
        self.__temperature = temperature
        return temperature

    def get_temp(self):
        return self.__temperature

    def set_fuel(self, fuel):
        self.__fuel = fuel
        return fuel

    def get_fuel(self):
        return self.__fuel


def main():
    vehicle1 = Car(0, 0, 0, 0)                                      # I don't understand why it has to be initialized with value but I imagine its because the class has this objects in the constructor
                                                                    # Set the fuel level
    f = input("How much fuel in car: ")

    vehicle1.set_fuel(f)                                            #I wanted to see if variable can be passed into the methods after asking for user input
                                                                    # Set the temperature
    t = input("Please enter ambient temperature desired: ")

    vehicle1.set_temp(t)
                                                                    # Set door amount
    d = input("Coupe (2) or Sedan(4). How many doors: ")

    vehicle1.set_doors(d)
                                                                    # Set wheel amount
                                                                    # Ask wheel amount
    w = input("How many wheels in the car : ")
    vehicle1.set_wheels(w)

    print("Creating vehicle....")
    time.sleep(1)
    print("This vehicle has,",vehicle1.get_fuel(),"gallons of fuel.")
    print("Ambient temperature inside your vehicel, set to ",vehicle1.get_temp(),".")
    print("Vehicle has ",vehicle1.get_doors(),"doors.")
    print("Vehicle has ",vehicle1.get_wheels(),"wheels.")
    print("Finalizing car registration...")
    time.sleep(1)
    print("Your vehicle object is now created. Have a nice day!")




    

main()






