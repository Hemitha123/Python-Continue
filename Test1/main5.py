FinalItemlist=[]
bill_list=[]
n=int(input("enter the number"))
for x in range(n):
    custid=int(input("enter the id of customer"))
    customer_name=input("enter the name")
    gender=input("enter the gender")
    item_name=input("enter the item name")
    category=input("enter the category")
    price_per_unit=int(input("enter the price per unit"))
    quantity=int(input("enter the quantity"))
    tup=(custid,customer_name,gender,item_name,category,price_per_unit,quantity)
    bill_list.append(tup)
#print(bill_list)
for item in bill_list:
    custid,customer_name,gender,item_name,category,price_per_unit,quantity=item
    amt=quantity*price_per_unit
    if category.lower()=="electronics":
        taxamt=amt*0.18
    elif category.lower()=="food":
        taxamt=amt*0.05
    else:
        taxamt=amt*0.15
    netamt=amt+taxamt
    tup=(custid,customer_name,gender,item_name,category,price_per_unit,quantity,amt,taxamt,netamt)
    FinalItemlist.append(tup)
print(FinalItemlist)
tddict={}
totnum=len(FinalItemlist)
print(f"Total customers did business is :{totnum}")
for x in FinalItemlist:
    gender=x[2]
    if tddict.get(gender)==None:
        tddict[gender]=1
    else:
        tddict[gender]+=1
for x in tddict:
    print(f"Total customer did business based on gender is {x},{tddict[x]}")
adict={}
for x in FinalItemlist:
    netamt=x[-1]
    category=x[4]
    if adict.get(category)==None:
        adict[category]=netamt
    else:
        adict[category]+=netamt
for x in adict:
    print(f"Total net amount collected is {x},{adict[x]}")
ddict={}
for x in FinalItemlist:
    taxamt=x[-2]
    category=x[4]
    if ddict.get(category)==None:
        ddict[category]=taxamt
    else:
        ddict[category]+=taxamt
for x in ddict:
    print(f"Total tax collected is:{x},{ddict[x]}")

category_name=""
highest=""
if category_name>highest:
    highest=category_name
print(f"the highest sold category is {category_name}")
high_male_item=""
high_female_item=""
male_name=""
female_name=""
for x in FinalItemlist:
    if gender=="m":
        if item_name>high_male_item:
            high_male_item=item_name
            male_name=customer_name
    else:
        if item_name>high_female_item:
            high_female_item=item_name
            female_name=customer_name
print(f"highest purchased item in Female is:{female_name}:{high_female_item}")
print(f"highest purchased item in Male is:{male_name}:{high_male_item}") 
   