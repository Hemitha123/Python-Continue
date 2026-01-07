class student:
    def __init__(self,name,marks):
        self.__name=name        #initialized
        self.__marks=marks
    def get_name(self):       #gets the name
        return self.__name
    def get_marks(self):      #gets the marks
        return self.__marks
    def set_marks(self,marks):
        if 0<=marks<=100:   #checks the condition
            self.__marks=marks
        else:
            return "Invalid Marks!"
s1=student("Amar",45)
print(f"Student name:{s1.get_name()}")
print(f"marks:{s1.get_marks()}")
s2=student("Ram",95)
print(f"Student name:{s2.get_name()}")
print(f"marks:{s2.get_marks()}")

s1.set_marks(50)        #modify the marks
print(f"Changed marks:{s1.get_marks()}")
s2.set_marks(90)
print(f"Changed marks:{s2.get_marks()}")
