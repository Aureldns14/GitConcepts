# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:15:28 2023

@author: doens
"""
import numpy as np

#ex1
a=np.arange(0,21)
a[9:16]=-a[9:16]
print(a)

#ex2
a=np.arange(15,56)
print(a[1:-1])

#ex3
m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i,j])

#ex4
a=np.linspace(5,50,10)
print(a)

#ex5
a=np.random.randint(0,11,5)
print(a)

#ex6
a=np.array([1,3,4,5])
b=np.array([2,5,3,2])
c=a*b
print(c)

#ex7
m=np.arange(10, 22).reshape(3, 4)
print(m)

#ex8
m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Number of rows = {}".format(len(m)))
print("Number of columns = {}".format(len(m[0])))

#ex9
m=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        m[i,j]=1
        if(i==j):
            m[i,j]=0
print(m)
        
#ex10
array1=[0, 10 ,20 ,40, 60]
array2=[10, 30, 40]
list=[]
for i in range(len(array2)):
    if array2[i] in array1:
        list.append(array2[i])
print(list)

#ex11
array1=np.array([10,10,20,20,30,30])
array2=np.array(([1,1],[2,3]))
list1=[]
list2=[]
for i in range(len(array1)):
    if array1[i] not in list1:
        list1.append(array1[i])
for i in range(len(array2)):
    for j in range(len(array2[0])):
        if array2[i,j] not in list2:
            list2.append(array2[i,j])
            
print("Original Array \n{} ".format(array1))
print("Unique Elements of the above array : \n{} ".format(list1))
print("Original Array \n{} ".format(array2))
print("Unique elements of the above array : \n{} ".format(list2))   

#ex12
vect1=np.array([1,3,7])
vect2=np.array([3,-1,10])
prod=np.cross(vect1,vect2)
print(prod)   

#ex14
vect=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49
,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74
,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
value=float(input("The value to compare : "))
list=[]
for i in range(len(vect)):
    if(value<=vect[i]):
        list.append(vect[i]-value)
    else:
        list.append(value-vect[i])
Array=np.array(list)
print(vect[Array.argmin()])   
    
            
