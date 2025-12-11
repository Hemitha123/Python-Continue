fname=open("C:/Python Hemitha/sampledata.txt")      #opens file 
head=fname.readline()    #reads one line and the pointer moves to next line
data=fname.readlines()    #reads the lines from the line where the pointer is 
print(head.strip())    #reamoves the space in head line
ddict={}    #empty dictionary which after stores the results 
for x in data:
    x=x.strip().split(',')#this removes the space after next line and also adds "," in between the elements
    print(x)
    sal=int(x[2])
    gen=x[3]
    if ddict.get(gen)==None:  #checks if dno present in ddict 
        ddict[gen]=(1,sal)  #if not then stores 
    else:
        ddict[gen]=(ddict[gen][0]+1,ddict[gen][1]+sal) 
        #if it is already present then it increment both employee and salary
fname.close()       #closes the file
print(f"total employees and total salary based on gender is:")
for x in ddict:
    print(x,ddict[x])
