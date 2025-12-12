#MultiLevel Inheritance

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f"Person name:{self.name}")
        print(f"Age of a Person:{self.age}")
    
class student(person):
    def __init__(self,name,age,roll_num):
        super().__init__(name,age)
        self.roll_num=roll_num

    def disrol(self):
        print(f"The roll number is:{self.roll_num}")
class exam(student):
    def __init__(self,name,age,roll_num,sub1,sub2,sub3):
        super().__init__(name,age,roll_num)
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def calculate_average(self):
        tot=self.sub1+self.sub2+self.sub3
        self.avg=tot//3

    def display(self):
        print(f"The Average of the marks is {self.avg}")

e1=exam("amar",23,101,87,90,94)
e1.intro()
e1.disrol()
e1.calculate_average()
e1.display()