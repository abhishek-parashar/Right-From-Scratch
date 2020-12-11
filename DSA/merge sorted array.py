# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:38:22 2020

@author: Abhishek Parashar
"""

arr1=[1, 3, 5, 7]
arr2=[2, 4, 6, 8]
arr3=[]
n1=len(arr1)
n2=len(arr2)
i=0
j=0

while(i<n1 and j<n2):
    if(arr1[i]<arr2[j]):
        arr3.append(arr1[i])
        i=i+1

    else:
        arr3.append(arr2[j])
        j=j+1
        
if(n1>n2):
    for i  in range(n2+1,n1+1):
        arr3.append(arr2[i])
elif(n2>n1):
    for i in range(n1+1,n2+1):
        arr3.append(arr2[i])
print(*arr3)
        
        
        