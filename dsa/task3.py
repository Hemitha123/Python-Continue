class employee:
    def __init__(self,id,ename,gender,dno,salary,tax):
        self.id=id
        self.ename=ename
        self.gender=gender
        self.dno=dno
        self.salary=salary
        self.tax=tax
        self.net_sal=self.cal_net_sal()
    def cal_net_sal(self):
        return self.salary-(self.salary*(self.tax/100))
    def display(self):
        print(f"ID:{self.id}")
        print(f"Name:{self.ename}")
        print(f"Gender:{self.gender}")
        print(f"Dno:{self.dno}")
        print(f"Salary:{self.salary}")
        print(f"Tax:{self.tax}")
        print(f"NetSalary:{self.net_sal}")
class Node:
    def __init__(self,emp):
        self.emp=emp          # assigning to the node
        self.next=None

class EmplList:
    def __init__(self):
        self.head=None     #initializing head to None
    def insert_beg(self,emp):
        new_node=Node(emp)  # Create a new node 
        new_node.next=self.head  # Next for new node becomes the current head
        self.head=new_node 
    def insert_end(self,emp):
        new_node=Node(emp)  # Create a new node
        if self.head is None:
            self.head=new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last=last.next
        last.next=new_node  # Make the new node the next node of the last node
    def printemp(self):
        temp=self.head # Start from the head of the list
        while temp:
            temp.emp.display() # Print the data in the current node
            temp=temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
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
while ch!=5:
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