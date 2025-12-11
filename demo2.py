#reads the file with readlines()

fname=open("C:/Python Hemitha/tabulardata.txt")
data=fname.readlines()
for x in data:
    print(x.strip())
fname.close()

#read and print the total salary of employee

fname=open("C:/Python Hemitha/tabulardata.txt")
head=fname.readline()
data=fname.readlines()
print(head.strip())
tot=0
for x in data:
    y=x.strip().split(',')
    print(y)
    tot+=int(y[2])
print(f"total salary of employee is:{tot}")
fname.close()