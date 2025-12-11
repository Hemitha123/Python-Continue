fname=open("C:/Python Hemitha/sampledata2.txt")  #opens the file
head=fname.readline()    #raed the single line which is head only and pointer moves to next line 
data=fname.readlines()    #read the lines from where the pointer is stoped
print(head.strip())    #removes the extra space 
sdict={}
for x in data:
    x=x.strip().split(',')   #removes extra space between the lines 
    print(x)
    g=x[1]
    p=x[2]
    if sdict.get(g)==None:   
        sdict[g]={}   #if the dictionary is empty then it is added
    if sdict[g].get(p)==None:
        sdict[g][p]=1
    else:
        sdict[g][p]+=1  #else it get incremented
fname.close()    #after reading the file it is closed
print("the total number of students based on gender and place is:")
for x in sdict:
    print(x,sdict[x])