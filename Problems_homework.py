# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:07:52 2023

@author: doens
"""

#S09_4
import numpy as np
array=np.linspace(1.0,5.0,21)
print("Values in Angstroms are : ")
print(array)
array=array*0.1
print("Values in Nanometers are : ")
print(array)

#S09_5
x0=int(input('The value of x0 : '))
s=float(input('The value of s : '))
i=int(input('The initial value of the interval : '))
f=int(input('The final value of the interval : '))
n=int(input('The number of points in the table : '))
x=np.linspace(i,f,n)
y=1/np.sqrt(2*np.pi)*np.exp(-0.5*((x-x0)**2/s**2))
print("x          y")
for i in range (0,n):
    print(round(x[i],3),"  ",round(y[i],5))
    
#S09_6
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
temp_mar_np=np.array(temp_mar)
av=np.average(temp_mar)
min=np.min(temp_mar)
ind1=temp_mar.index(min)
max=np.max(temp_mar)
ind2=temp_mar.index(max)
print("The average sea surface temperature in 2014 : {}°C.".format(round(av,1)))
print("The month in which the sea surface has been coldest and its temperature : {} / {}°C.".format(months[ind1],min))
print("The month in which the sea surface has been warmest and its temperature : {} / {}°C.".format(months[ind2],max))

#S09_10
n=int(input("The number of students : "))
theory_grade=[]
problem_grade=[]
total_grade=[]
for i in range(0,n):
    theory=float(input("The theory score of the student {} : ".format(i+1)))
    problem=float(input("The problem score of the student {} : ".format(i+1)))
    total=theory*0.40+problem*0.60
    total=round(total,2)
    theory_grade.append(theory)
    problem_grade.append(problem)
    total_grade.append(total)
    print("___________")

print("Index   Theory  Problem    Total")
for i in range(0,n):
    print("{}       {}       {}       {}".format(i,theory_grade[i],problem_grade[i],total_grade[i]))
    
average=np.average(total_grade)
min=np.min(total_grade)
max=np.max(total_grade)
average=round(average,2)
print("The average is : {}/10.".format(average))
print("The minimum grade is : {}/10.".format(min))
print("The maximum grade is : {}/10.".format(max))