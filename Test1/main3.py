#1.
def fn_ndbiggest(llist):
    llist=list(set(llist))
    llist.sort()
    return llist[-2]
lnum=[10,50,30,50,40,20,10,100]
print(f"the second biggest number is:{fn_ndbiggest(lnum)}")

#2.
def fn_vowel(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
mystr=input("enter the string")
print(fn_vowel(mystr))
    

#3.
num=int(input("enter the number"))
for i in range(10,0,-1):
    print(f"{num}x{i}={num*i}")

#4.
n=int(input("enter the number"))
llist1=[]
for x in range(n):
    m=int(input("enter the numbre of elements"))
    llist1.append(m)
print(llist1)
n=int(input("enter the number"))
llist2=[]
for x in range(n):
    m=int(input("enter the numbre of elements"))
    llist2.append(m)
print(llist2)
llist3=[]
for x in llist1:
    if x%2==0:
        llist3.append(x)
for x in llist2:
    if x%2==0:
        llist3.append(x)
print(llist3)

#5.
glist=["Mr.Rama","Miss.Rani","Miss.Hemitha","Mr.Ronith","Miss.Siya","Mr.Ramesh","Mr.Ravi","Mr.Lohith","Miss.Riya","Miss.Punya"]
mlist=[]
flist=[]
for x in glist:
    if x.startswith("Mr"):
        mlist.append(x)
    elif x.startswith("Miss"):
        flist.append(x)
    else:
        print("Invalid")
print(mlist)
print(flist)


#6.
def fn_fib(n):
    a=0
    b=1
    f=[]
    for x in range(n):
        f.append(a)
        a,b=b,a+b
    return f 
n=int(input("enter the number"))
print(fn_fib(n))


#7.
def fn_student(ddict):
    c_count={}
    for st_id,(name,course) in ddict.items():
        if course not in c_count:
            c_count[course]=1
        else:
            c_count[course]+=1
    return c_count
ddict={}
n=int(input("enter the number"))
for x in range(n):
    st_id=int(input("enter the student id"))
    name=input("enter the name")
    course=input("enter the course")
    ddict[st_id]=(name,course)
print(fn_student(ddict))


#8.
namelist = [("Amar","m"),("sheela","f"),("Kumar","m"),("rita","f"),("Venu","m")]
new_list=[]
for name,gender in namelist:
    if gender=="m":
        new_list.append("Mr"+"."+name)
    else:
        new_list.append("Mis"+"."+name)
print(new_list)

#9.
glist = ["10000","20000","3500s","4500O","5000I","60000","70000"]
nlist=[]
for x in glist:
    if x.isnumeric():
        nlist.append(int(x))
print(nlist)
tot=sum(nlist)
print(f"the sum of numbers in the list is {tot}")


#10.
def fn_asc(string):
    newlist=[]
    ch=""
    for ch in string:
        newlist.append(ord(ch))
    return newlist
string=input("enter the string")
print(fn_asc(string))