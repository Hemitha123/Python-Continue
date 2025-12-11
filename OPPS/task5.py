#Simple inheritance

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age    #inisialized the attributes
    
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")     
    
class student(person):
    def __init__(self,name,age,roll_num):
        super().__init__(name,age)    #super function is used to call the attributes name,age from class person
        self.roll_num=roll_num
    
    def display(self):
        print(f"The roll number of {self.name} is:{self.roll_num}")

s1=person("ram",23)
s1.introduce()
s2=student("ram",23,101)
s2.display()