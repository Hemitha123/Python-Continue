class Node:
    def _init_(self,emp):
        self.emp = emp          # assigning to the node
        self.next = None
class EmplList:
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
    def insertAtBeginning(self, new_data):
        new_node = Node(emp)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node 
    def insertAtEnd(self,emp):
        new_node = Node(emp)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
    def printemp(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
    def search(self,id):
        current = self.head  # Start with the head of the list
        position = 1  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"ID {self.id} found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"ID {self.id}"