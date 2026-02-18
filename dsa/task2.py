class Node:
    def __init__(self, data):
        self.data = data    #assigns the data to the node
        self.next = None     #initialize to null
        
class LinkedList:
    def __init__(self):
        self.head = None     #initialize head as None
        
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)   #create a new node 
        new_node.next = self.head   
        self.head = new_node    
        
    def printList(self):
        temp = self.head     #start from the head
        while temp:
            print(temp.data,end=' ')     #print the data 
            temp = temp.next     #move to the next node
        print()     
        
    def insertAtEnd(self, new_data):
        new_node = Node(new_data) 
        if self.head is None:
            self.head = new_node    
            return
        last = self.head 
        while last.next:    
            last = last.next
        last.next = new_node    
        
    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty"          #if the list is empty,return this string
        self.head = self.head.next                 
    def deleteFromEnd(self): 
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None      
            return
        temp = self.head
        while temp.next.next:  
            temp = temp.next
        temp.next = None   
    
    def search(self, value):
        current = self.head      #start with the head of the list
        position = 1        #counts position
        while current: 
            if current.data == value: 
                return f"Value '{value}' found at position {position}"
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list"
llist=LinkedList()
ch=0
while ch!=7:
    print("1.insert data at begining")
    print("2.insert data at end")
    print("3.delete data at beginning")
    print("4.delete data at end")
    print("5.display data")
    print("6.search data")
    print("7.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        a=input("enter the data")
        llist.insertAtBeginning(a)
    elif ch==2:
        b=input("enter the data")
        llist.insertAtEnd(b)
    elif ch==3:
        msg=llist.deleteFromBeginning()
        if msg:
            print(msg)
    elif ch==4:
        msg=llist.deleteFromEnd()
        if msg:
            print(msg)
    elif ch==5:
        llist.printList()
    elif ch==6:
        f=input("enter the data")
        print(llist.search(f))
    else:
        print("Exit")
        break
