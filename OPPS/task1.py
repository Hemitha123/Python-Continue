class student():    #craeted class name student 
    def __init__(self,name,gender,s1,s2,s3):  #initializes the variables
        self.name=name     
        self.gender=gender
        self.s1=s1
        self.s2=s2
        self.s3=s3  #assigns the value accordingly to the variables
    def sub_tot(self):   #method called sub_tot
        self.tot=self.s1+self.s2+self.s3   #calculates the total
    def sub_avg(self):   #method called sub_avg
        self.avg=self.tot//3    #calculataes the avg
    def sub_grade(self):   #method called sub_grade
        if 80<self.avg<100:
            self.grade="A"
        elif 60<self.avg<80:
            self.grade="B"
        else:
            self.grade="F"   #checks for the condition==True
    def stud_details(self):    #method called stud_details
        print(f"Student name:{self.name}")
        print(f"Gender:{self.gender}")   #prints all the values assigned
    
    def marks_details(self):
        print(f"Subject1:{self.s1}")
        print(f"Subject2:{self.s2}")
        print(f"Subject3:{self.s3}")
        print(f"Total:{self.tot}")
        print(f"Average:{self.avg}")
        print(f"Grade:{self.grade}")

student1=student("hemitha","f",90,87,83)  #input
student1.stud_details()  #methods are called 
student1.sub_tot()
student1.sub_avg()
student1.sub_grade()
student1.marks_details()