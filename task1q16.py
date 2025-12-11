fname=open("C:/Python Hemitha/sampledata3.txt")
head=fname.readline()
data=fname.readlines()
print(head.strip())
flist=[]
ddict={}
for x in data:
    x=x.strip().split(',')
    print(x)
    name=x[0]
    gender=x[1]
    branch=x[2]
    s1=int(x[3])
    s2=int(x[4])
    s3=int(x[5])
    s4=int(x[6])
    s5=int(x[7])
    s6=int(x[8])
    tot=s1+s2+s3+s4+s5+s6
    avg=tot//6
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
mcount=0
fcount=0
mtotal=0
ftotal=0
for x in flist:
    print(x)
    gender=x[1]
    grade=x[-1]
    if gender=="m":  #counts the number of students based on gender
        mcount+=1
    else:
        fcount+=1
    if grade!="Fail":   #enter if it is pass
        if gender=="m":   #counts the total number of students passed 
            mtotal+=1
        elif gender=="f":
            ftotal+=1
fname.close()
print(f"the persentage is:{(mtotal/mcount)*100}%")
print(f"the persentage is:{(ftotal/fcount)*100}%")