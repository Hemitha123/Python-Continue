fname=open("C:/Python Hemitha/sampledata.txt")      #opens the file 
head=fname.readline()    #reads one line and the pointer moves to next line
data=fname.readlines()    #reads the lines from the line where the pointer is 
print(head.strip())    #reamoves the space in head line
edict={}    #empty dictionary 
for x in data:
    x=x.strip().split(',')#this removes the space after next line and also adds "," in between the elements
    print(x)
    dno=x[4]
    if edict.get(dno)==None:  #checks if dno present in ddict 
        edict[dno]=1    #if not then stores 
    else:
        edict[dno]+=1      #if it is already present then it increment
fname.close()       #closes the file
print(f"the number of employee based on department number is:")
for x in edict:
    print(f"Dno:{x},number:{edict[x]}")
