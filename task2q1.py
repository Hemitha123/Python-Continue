dfile=open("C:/Python Hemitha/deptfile.txt")   #opens the file
dhead=dfile.readline()   #reads the single line and moves to next line
ddata=dfile.readlines()   #reads from where the pointer stoped
#print(dhead.strip())
ddict={}   #empty dictionary
for x in ddata:
    x=x.strip().split(',')
    #print(x)
    ddict[x[0]]=x[1]   #creates the given data to dictionary format
dfile.close()   #closes the file
#print(ddict)


pfile=open("C:/Python Hemitha/placemaster.txt")
phead=pfile.readline()
pdata=pfile.readlines()
#print(phead.strip())
pdict={}
for x in pdata:
    x=x.strip().split(',')
    #print(x)
    pdict[x[0]]=x[1]    #creats the data to dictionary format
pfile.close()
#print(pdict)


efile=open("C:/Python Hemitha/empfile.txt")
ehead=efile.readline()
edata=efile.readlines()
#print(ehead.strip())
elist=[]   #empty list
for x in edata:
    x=x.strip().split(',')
    #print(x)
    dname=ddict.get(x[-2])   #converts the index i.e x[-2] which is dno to dname
    placename=pdict.get(x[-1])   #coverts the index i.e x[-1] which is idplace to placename
    tup=(x[0],x[1],x[2],x[3],dname,placename) #it tells to read dname and placename 
    elist.append(tup)  #dname and placename is appended to elist
efile.close()   #closes the file
for x in elist:
    print(x)   #prints the output
    