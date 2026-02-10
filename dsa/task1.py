class stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
S=stack()
print(S.isEmpty())
try:
    S.push(2)
    S.push(4)
    S.push(6)
    S.push(8)
    print(S.items)

    print(S.isEmpty())

    S.pop()
    print(S.items)
except IndexError:
    print("No Item.Pop from empty list")
try:
    S.peek()
    print(S.items)
except IndexError:
    print("No Item.List index out of range")
else:
    print("Done")
print(len(S.items))
