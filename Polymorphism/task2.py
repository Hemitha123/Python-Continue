#Inheritance Polymorphism

class Shape:
    def area(self):
        print("Area of the Shapes")

class rectangle(Shape):
    def __init__(self,length,width):    #initialization
        self.length=length
        self.width=width
    def cal_area(self):
        a=self.length*self.width     #calculates the area of rectangle
        print(f"Area of rectangle is {a}")

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def cal_area(self):
        a=float(3.14*self.radius**2)    #calculates the area of circle
        print(f"Area of circle is {a}")

Rectangle=rectangle(20,30)
Circle=circle(6)
Rectangle.area()
Rectangle.cal_area()
Circle.area()
Circle.cal_area()