class stack():  #class stack
    def __init__(self):     #initialization of items
        self.items=[]
    def isEmpty(self):
        return self.items==[]          #if it is empty then it show true else false
    def push(self,item):
        self.items.insert(0,item)       #adds or inserts the item 
    def pop(self):
        self.items.pop(0)           #removes only the last item 
    def peek(self):
        return self.items[0]        #shows only the first item
    def size(self):
        return len(self.items)      #shows the len of  the stack
S=stack()       #object called S
print(S.isEmpty())
try:
    # S.push(2)
    # S.push(4)
    # S.push(6)
    # S.push(8)
    # print(S.items)

    # print(S.isEmpty())

    S.pop()
    print(S.items)
except IndexError:      #a condition that raises error statement instead of error in the program
    print("No Item.Pop from empty list")
try:
    S.peek()
    print(S.items)
except IndexError:
    print("No Item.List index out of range")
else:
    print("Done")       #if the program runs without an error this statement shows off
print(len(S.items))
