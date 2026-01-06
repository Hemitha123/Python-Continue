#Class Polymorphism

class car:
    def move(self):
        print("Car drives on road")

class bike:
    def move(self):
        print("Bike rides on road")
Car=car()
Bike=bike()
# Car.move()
# Bike.move()
for x in (Car,Bike):
    x.move()