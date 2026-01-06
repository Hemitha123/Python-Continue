#Transport System

class transport():
    def __init__(self,distance):       #initialization
        self.distance=distance
    def fare(self):
        print("The Fare for different transport")
class bus(transport):
    def fare(self):
        f=self.distance*10      #calculates the distance
        print(f"The fare for Bus transport is {f}")
class train(transport):
    def fare(self):
        f=self.distance*5
        print(f"The fare for Train transport is {f}")
class flight(transport):
    def fare(self):
        f=self.distance*50
        print(f"The fare for Flight transport is {f}")

Transport=transport(100)
Transport.fare()
Bus=bus(30)
Train=train(50)
Flight=flight(200)
for x in (Bus,Train,Flight):
    x.fare()