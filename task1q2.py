fname=open("C:/Python Hemitha/sampledata.txt")      #opens the file
head=fname.readline()    #reads one line and the pointer moves to next line
data=fname.readlines()    #reads the lines from the line where the pointer is 
print(head.strip())    #reamoves the space in head line
ndict={}    #empty dictionary  
for x in data:
    x=x.strip().split(',')#this removes the space after next line and also adds "," in between the elements
    print(x)
    n=x[1]
    dno=x[4]
    if ndict.get(dno)==None:  #checks if dno present in ddict 
        ndict[dno]=[n]      #if not then stores 
    else:
        ndict[dno]+=[n]      #if it is already present then it increment
fname.close()       #closes the file
print(f"the name of employee based on department number is:")
for x in ndict:
    print(f"Dno:{x},Name:{ndict[x]}")