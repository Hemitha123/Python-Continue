class stack():
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def push(self):
        self.item.insert(0,item)
    def pop(self):
        self.item.pop(0)
    def peek(self):
        return self.item[0]
    def size(self):
        return len(self.item)
S=stack()
print(S.isEmpty())
S.push(2)
S.push(4)
S.push(6)
S.push(8)

for x in S.items:
    print(x)

print(S.isEmpty())

S.pop(2)
for x in S.items:
    print(x)
S.push(10)
for x in S.items:
    print(x)
S.pop()
for x in S.items:
    print(x)
print(len(S.items))
