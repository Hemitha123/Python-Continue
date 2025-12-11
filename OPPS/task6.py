#MultiLevel Inheritance

class animal():    #class
    def sound(self):    #method
        print("The sound of animals")

class dog(animal):
    def sound(self):
        print("Dog:Woof")
    
class puppy(dog):
    def sound(self):
        print("Puppy:Yip")

a1=animal()    #object
a1.sound()
a2=dog()
a2.sound()
a3=puppy()
a3.sound()
