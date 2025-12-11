#Multiple Inheritance

class teacher():
    def teach(self):
        print("Teacher teaches subject to the students")

class Mentor():
    def guide(self):
        print("Guide, guides the students")

class Tutor(teacher,Mentor):
    def __init__(self,subject):
      self.subject=subject

    def display(self):
        print(f"Tutor teaches {self.subject} and also guides students in projects")

t1=Tutor("Python")
t1.teach()
t1.guide()
t1.display()