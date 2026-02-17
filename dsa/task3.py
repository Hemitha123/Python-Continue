class employee:
    def __init__(self,id,ename,gender,dno,salary,tax):      #initialization
        self.id=id
        self.ename=ename
        self.gender=gender
        self.dno=dno
        self.salary=salary
        self.tax=tax
        self.net_sal=self.cal_net_sal()
    def cal_net_sal(self):      #calculates the net salary
        return self.salary-(self.salary*(self.tax/100))
    def display(self):
        print(f"ID:{self.id}")
        print(f"Name:{self.ename}")
        print(f"Gender:{self.gender}")
        print(f"Dno:{self.dno}")
        print(f"Salary:{self.salary}")
        print(f"Tax:{self.tax}")
        print(f"NetSalary:{self.cal_net_sal()}")
class Node:
    def __init__(self,emp):
        self.emp=emp          #assigs to the node
        self.next=None

class EmplList:
    def __init__(self):
        self.head=None     #initializing head to None
    def insert_beg(self,emp):
        new_node=Node(emp)  #creates a new node 
        new_node.next=self.head  
        self.head=new_node 
    def insert_end(self,emp):
        new_node=Node(emp) 
        if self.head is None:
            self.head=new_node  
            return
        last = self.head 
        while last.next: 
            last=last.next
        last.next=new_node  
    def printemp(self):
        temp=self.head 
        while temp:
            temp.emp.display() #prints the employee details
            temp=temp.next  #moves to next node
        print() 
    def search(self,id):
        current=self.head
        found=False
        while current:
            if current.emp.id==id:
                print("Employee found")
                current.emp.display()
                found=True
                break
                current=current.next
            if not found:
                print("Not found")
emp_list=EmplList()
ch=0
while ch!=5:            #menu function
    print("1. Insert Employee at Beginning")
    print("2. Insert Employee at End")
    print("3. Display Employees")
    print("4. Search Employee by ID")
    print("5. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1 or ch==2:
        id=int(input("Enter ID: "))
        name=input("Enter Name: ")
        gender=input("Enter Gender: ")
        dno=int(input("Enter dno: "))
        salary=int(input("Enter Salary: "))
        tax=int(input("Enter Tax %: "))
        emp=employee(id, name, gender, dno, salary, tax)
    if ch==1:
        emp_list.insert_beg(emp)   
    elif ch==2:
        emp_list.insert_end(emp)
    elif ch==3:
        emp_list.printemp()
    elif ch==4:
        s=int(input("Enter Employee ID to search: "))
        emp_list.search(s)
    else:
        print("Exit")
        break