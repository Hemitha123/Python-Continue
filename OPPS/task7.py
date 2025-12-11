#Hierarchical Inheritance
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"The Employee name is {self.name}")
        print(f"The salary of Employee is {self.salary}")

class developer(employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language

    def work(self):
        print(f"{self.name} uses {self.language} to develop a software")

class designer(employee):
    def __init__(self,name,salary,tool):
        super().__init__(name,salary)
        self.tool=tool

    def work(self):
        print(f"{self.name} uses {self.tool} to design a software")

e1=developer("amar",50000,"python")
e1.work()
e2=designer("ankitha",70000,"pycharm")
e2.work()