fname=open("C:/Python Hemitha/sampledata3.txt")   #opens the file
head=fname.readline()   #reads first line
data=fname.readlines()   #reads the lines from where point stops
print(head.strip())
flist=[]   #empty list
ddict={}    #empty dictionary
for x in data:
    x=x.strip().split(',')
    print(x)
    name=x[0]    #inisialized with index
    gender=x[1]
    branch=x[2]
    s1=int(x[3])
    s2=int(x[4])
    s3=int(x[5])
    s4=int(x[6])
    s5=int(x[7])
    s6=int(x[8])
    tot=s1+s2+s3+s4+s5+s6   #totals the marks
    avg=tot//6     #averages the marks 
    if (s1<35 or s2<35 or s3<35 or s4<35 or s5<35 or s6<35):
        grade="Fail"
    elif 80<=avg<=100:
        grade="A"
    elif 70<=avg<=79:
        grade="B"
    elif 60<=avg<=69:
        grade="C"
    elif 35<=avg<=59:
        grade="D"
    else:
        grade="F"
    flist.append((name,gender,branch,s1,s2,s3,s4,s5,s6,tot,avg,grade))
for x in flist:
    print(x)
    grade=x[-1]
    if ddict.get(grade)==None:   #checks if the dictionary has grade 
        ddict[grade]=1   #if not present then it is appended
    else:
        ddict[grade]+=1   #if it is already present then it is incremented 
fname.close()
for x in ddict:
    print(x,ddict[x])