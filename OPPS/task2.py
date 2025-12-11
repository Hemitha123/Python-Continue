class student():   #class called student
    def __init__(self,name,roll_number,marks):   
        self.name=name
        self.roll_number=roll_number
        self.marks=marks   #initializing the variables
        
    def display_info(self):   #method display_info()
        print(f"Student Name is:{self.name}")
        print(f"Student roll number:{self.roll_number}")
        print(f"Marks scored by Student:{self.marks}")
        
    def calculate_grade(self):     #method calculate_grade()
        if 80<self.marks<=100:     #Checks the condition
            self.grade="A"
        elif 60<self.marks<=80:
            self.grade="B"
        elif 40<self.marks<=60:
            self.grade="C"
        elif 35<self.marks<=40:
            self.grade="D"
        else:
            self.grade="F"
        print(f"The grade is:{self.grade}")
s1=student("amar","S123",60)   #input
s2=student("hitha","S345",99)
s3=student("rani","S567",32)
s4=student("raj","S456",45)
s1.display_info()             #method is called
s1.calculate_grade()
s2.display_info()
s2.calculate_grade()
s3.display_info()
s3.calculate_grade()
s4.display_info()
s4.calculate_grade()