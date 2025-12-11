fname=open("C:/Python Hemitha/sampledata2.txt")  #opens the file
head=fname.readline()    #raed the single line which is head only and pointer moves to next line 
data=fname.readlines()    #read the lines from where the pointer is stoped
print(head.strip())    #removes the extra space 
sdict={}
for x in data:
    x=x.strip().split(',')   #removes extra space between the lines 
    print(x)
    p=x[2]
    c=x[-2]
    if sdict.get(p)==None:  
        sdict[p]={}
    if sdict[p].get(c)==None:
        sdict[p][c]=1   #if the dictionary is empty then it is added
    else:
        sdict[p][c]+=1  #else it get incremented
fname.close()    #after reading the file it is closed
print("the total number of students based on place and course is:")
for x in sdict:
    print(x,sdict[x])