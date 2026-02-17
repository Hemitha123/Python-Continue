class Node:
    def _init_(self,emp):
        self.emp = emp          # assigning to the node
        self.next = None
class LinkedList:
        def _init_(self):
            self.head = None     #initializing head to None
class employee:
    def __init__(self,id,ename,gender,dno,salary,tax):
        self.id=id
        self.ename=ename
        self.gender=gender
        self.dno=dno
        self.salary=salary
        self.tax=tax
        self.net_sal=net_sal
    def cal_net_sal(self):
        net_sal=self.salary-(self.salary*(self.tax/100))
    def display(self):
        print("ID":self.id)
        print("Name":self.ename)
        print("Gender":self.gender)
        print("Dno":self.dno)
        print("Salary":self.salary)
        print("Tax":self.tax)
    def 