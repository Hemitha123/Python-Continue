vdict={}
hassan_count={}
out_count={}
m_count={}
n=int(input("enter the number"))
for x in range(n):
    reg_no=input("enter the reg no")
    name=input("enter the name")
    age=int(input("enter the age"))
    place=input("enter the palce")
    model=input("enter the model")
    vdict[reg_no]=(name,age,place,model)
print(vdict)
for y in vdict:
    place=vdict[y][2]
    if place.lower()=="hassan":
        if hassan_count.get(place)==None:
            hassan_count[place]=1
        else:
            hassan_count[place]+=1
    else:
        if out_count.get(place)==None:
            out_count[place]=1
        else:
            out_count[place]+=1
print(f"total number of vehicle registered in hassan:{hassan_count}")
print(f"total number of vehicle registered from outside:{out_count}")
for x in vdict:
    model=vdict[x][3]
    if m_count.get(model)==None:
        m_count[model]=1
    else:
        m_count[model]+=1
print(f"Model count:{m_count}")


empname=["amar","ram","rani","ramesh","arun","anish","sunil","siya","riya","hemitha"]
gender=["m","m","f","m","m","m","m","f","f","f"]
designation=["maneger","hr","admin","technical","admin","hr","maneger","hr","technical","maneger"]
salary=["50000","40000","30000","25000","30000","40000","50000","30000","25000","50000"]
emplist=[]
for x in range(10):
    sal=int(salary[x])
    hra=sal*0.10
    cca=sal*0.05
    grossalary=sal+hra+cca
    incometax=sal*0.08
    netsalary=grossalary-incometax
    newtup=(empname[x],gender[x],designation[x],sal,hra,cca,grossalary,incometax,netsalary)
    emplist.append(newtup)
for x in emplist:
    print(x)


custdict={101:("amar",50000),102:("siya",45000),103:("riya",20000),104:("ramesh",50000),105:("venu",34000)}
trandict={101:(40000,"cr"),102:(5000,"dr"),103:(2500,"cr"),104:(4000,"dr"),105:(3500,"cr")}
curbaldict={}
for accno,cust in custdict.items():
    name,bal=cust
    for accno,transac in trandict.items():
        amt,value=transac
        if value=="cr":
            cubal=amt+bal
        else:
            cubal=bal-amt
        curbaldict[accno]=(name,cubal)
print(curbaldict)



newlist=[]
n=int(input("enter the number"))
for x in range(n):
    name=input("enter the name")
    place_to_travel=input("enter the place")
    ticket_fare=int(input("enter the fare"))
    tup=(name,place_to_travel,ticket_fare)
    newlist.append(tup)
print(newlist)
ddict={}
for x in newlist:
    name=x[0]
    place=x[1]
    if ddict.get(place)==None:
        ddict[place]=1
    else:
        ddict[place]+=1
for x in ddict:
    print(x,ddict[x])
tdict={}
for x in newlist:
    ticket_fare=x[-1]
    place=x[1]
    if tdict.get(place)==None:
        tdict[place]=ticket_fare
    else:
        tdict[place]+=ticket_fare
for x in tdict:
    print(x,tdict[x]) 
