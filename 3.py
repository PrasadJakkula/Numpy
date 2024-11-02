import numpy as np
#Creating an  array.
a = np.arange(10)#Gives a array of 10 elements from 0-9
print(a)
print(a.shape)
print(" ")

#Multidimensional  numpy array.
b = np.array([np.arange(3),np.arange(3)])#Creates 2 row and 3 columns
print(b)
print(b.shape)
print(" ")

#Creating a three-by-three array
m = np.array([np.arange(10),np.arange(10),np.arange(10)])#3rows and 3columns
print(m)
print(m.shape)
print(" ")

#Giving what elements we need in the array.
n = np.array([[1,2],[2,3]])#2 rows and 2columns
print(n)
l = n[0,0]#1st element that is 1
m = n[0,1]#2nd element
o = n[1,0]#3rd
p = n[1,1]#4th
print(l)
print(m)
print(o)
print(p)
print(" ")

#Giving a threexthree matrics of desired elements
a = np.array([[1,2,3],[3,4,5],[5,6,7]])#3row and 3columns
print(a)
print(a.shape)
print(a[0,0])#1st element
print(a[0,1])#2nd
print(a[0,2])#3rd
print(a[1,2])#6th
