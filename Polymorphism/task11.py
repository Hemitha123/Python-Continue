import numpy as np 
matrix=np.arange(25).reshape(5,5)
print(matrix)

#extract 12,13 and 17,18
print(matrix[2:4,2:4])

#extract 10,11 and 15,16
print(matrix[2:4,0:2])

#extract 1,2 and 6,7
print(matrix[0:3,1:3])

#extract 18,19 and 23,24
print(matrix[3:,3:])

#extract 8,9 and 13,14
print(matrix[1:3,3:5])

#extract 17,18 and 22,23
print(matrix[3:,2:4])

#extract 16,17 and 21,22
print(matrix[3:,1:3])

#extract 15,16 and 20,21
print(matrix[3:5,0:2])

#extract 2,3 and 7,8
print(matrix[0:2,2:4])

#extract 13,14 and 18,19
print(matrix[2:4,3:])



