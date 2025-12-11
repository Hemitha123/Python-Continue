dfile=open("C:/Python Hemitha/deptfile.txt")
dhead=dfile.readline()
ddata=dfile.readlines()
#print(dhead.strip())
ddict={}
for x in ddata:
    x=x.strip().split(',')
    #print(x)
    ddict[x[0]]=x[1]
dfile.close()
print(ddict)


efile=open("C:/Python Hemitha/empfile.txt")
ehead=efile.readline()
edata=efile.readlines()
#print(ehead.strip())
flist=[]
for x in edata:
    x=x.strip().split(',')
    #print(x)
    dname=ddict.get(x[-2])
    tup=(x[0],x[1],x[2],x[3],dname,x[5])
    flist.append(tup)
efile.close()
for x in flist:
    print(x)