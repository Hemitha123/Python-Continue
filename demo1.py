#read the file using number of bytes to be read and close

fname=open("C:/Python Hemitha/sample.txt")
data=fname.read(10)
data2=fname.read()
print(data)
print(data2)
fname.close()

#read the file using seek and close

fname=open("C:/Python Hemitha/sample.txt")
fname.seek(20)
data=fname.read()
print(data)
fname.close()

#read file using readlines()

fname=open("C:/Python Hemitha/sample.txt")
data=fname.readline()
print(data)
fname.close()

#read file using readlines()

fname=open("C:/Python Hemitha/sample.txt")
data=fname.readlines()
for x in data:
    print(x.strip())
fname.close()

