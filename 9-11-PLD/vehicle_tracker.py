#!/usr/bin/python3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def details(self):
        print("The {} {} {} has {} doors!".format(self.year, self.make, self.model, self.number_of_doors))

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar=False):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def details(self):
        if self.has_sidecar == True:
            print("The {} {} {} does have a sidecar!".format(self.year, self.make, self.model))
        else:
            print("The {} {} {} does not have a sidecar!".format(self.year, self.make, self.model))

vehicle1 = Car("Honda", "Accord", 2014, 4)
vehicle2 = Motorcycle("Harley Davidson", "SPORTSTER", 2010)
vehicle3 = Motorcycle("Voger", "250 Street Ready Cruiser", 2007, True)

vehicle1.details()
vehicle2.details()
vehicle3.details()
