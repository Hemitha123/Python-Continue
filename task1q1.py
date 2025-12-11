fname=open("C:/Python Hemitha/sampledata.txt")      #it goes through the path given and opens file 
head=fname.readline()    #reads one line and the pointer moves to next line
data=fname.readlines()    #reads the lines from the line where the pointer is 
print(head.strip())    #reamoves the space in head line
ddict={}    #empty dictionary which after stores the results 
for x in data:
    x=x.strip().split(',')#this removes the space after next line and also adds "," in between the elements
    print(x)
    sal=int(x[2])
    dno=x[4]
    if ddict.get(dno)==None:  #checks if dno present in ddict 
        ddict[dno]=sal      #if not then stores 
    else:
        ddict[dno]+=sal      #if it is already present then it increment
fname.close()       #closes the file
print(f"the salary of employee based on department number is:")
for x in ddict:
    print(f"Dno:{x},salary:{ddict[x]}")