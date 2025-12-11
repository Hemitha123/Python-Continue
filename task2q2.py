pfile=open("C:/Python Hemitha/placemaster.txt")
phead=pfile.readline()
pdata=pfile.readlines()
#print(phead.strip())
pdict={}
for x in pdata:
    x=x.strip().split(',')
    #print(x)
    pdict[x[0]]=x[1]    
pfile.close()
#print(pdict)

bfile=open("C:/Python Hemitha/branchmaster.txt")
bhead=bfile.readline()
bdata=bfile.readlines()
#print(bhead.strip())
bdict={}
for x in bdata:
    x=x.strip().split(',')
    #print(x)
    bdict[x[0]]=x[1]    
bfile.close()
#print(bdict)

ffile=open("C:/Python Hemitha/feedetails.txt")
fhead=ffile.readline()
fdata=ffile.readlines()
#print(fhead.strip())
fdict={}
for f in fdata:
    f=f.strip().split(',')
    #print(f)
    fdict[f[1]]=int(f[2])    
ffile.close()
#print(fdict)

sfile=open("C:/Python Hemitha/studentmaster.txt")
shead=sfile.readline()
sdata=sfile.readlines()
#print(shead.strip())
slist=[]
bal=0
for s in sdata:
    s=s.strip().split(',')
    #print(x)
    placename=pdict.get(s[3])
    branchname=bdict.get(s[4])
    paid=fdict.get(s[0])
    fee=int(s[-1])
    bal=fee-paid    #to get balance subtract fee with paid amount
    tup=(s[0],s[1],s[2],placename,branchname,fee,paid,bal) 
    slist.append(tup)  #append the tup to list
sfile.close()
for x in slist:
    print(x)
    