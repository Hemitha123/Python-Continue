#1.
a="Hello my name is APJ Abdul Kalam"
b=a[:5]
c=a[-15:-12]
d=a[-5:]
print(b)
print(c)
print(d)

#2b.
a=int(input("enter the number"))
b=int(input("enter the number"))
c=(a+b)**2
print(c)

#3.
x=int(input("enter the number"))
while x>-1:
    print(x,end="")
    x-=1

#4.
a=int(input("enter the number"))
b=int(input("enter the number"))
if a%2!=0 and b%2!=0:
    c=a+b
    print("the given numbers are odd numbers")
    print(f"the sum of the numbers are {c}")
else:
    print("the given numbers are even numbers")

#5.
mysen=input("enter a sentence(min 10 words)")
word=mysen.split()
big=""
if len(word)<10:
    print("please enter the sentence with min 10 words")
for x in word:
    if len(x)>len(big):
        big=x
print(f"biggest word is:{big}")