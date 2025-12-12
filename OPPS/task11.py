#Hierarchical Inheritance
class employee():
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary
    def intro(self):
        print(f"the name is:{self.name}")
        print(f"the basic salary is:{self.basic_salary}")
    def calculate_bonus(self):
        self.bonus=self.basic_salary*0.10
    def disbon(self):
        print(f"The bonus is:{self.bonus}")
class developer(employee):
    def __init__(self,name,basic_salary,lines_of_code):
        super().__init__(name,basic_salary)
        self.lines_of_code=lines_of_code
    def productivity_score(self):
        self.loc=(self.lines_of_code)/100
    def disloc(self):
        print(f"The productivity score is:{self.loc}")
class manager(employee):
    def __init__(self,name,basic_salary,team_size):
        super().__init__(name,basic_salary)
        self.team_size=team_size
    def team_allowance(self):
        self.ta=self.team_size*500
    def dista(self):
        print(f"The team allowance is:{self.ta}")
e1=developer("amar",50000,1000)
e1.intro()
e1.calculate_bonus()
e1.disbon()
e1.productivity_score()
e1.disloc()
e2=manager("rohit",70000,6)
e2.intro()
e2.calculate_bonus()
e2.disbon()
e2.team_allowance()
e2.dista()