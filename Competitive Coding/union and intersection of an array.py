# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:13:58 2020

@author: Abhishek Parashar
"""

arr1=[2,85]
arr2=[1,6,25,34,54,85]
a=[]
n=2
m=6
i=0
j=0
while(i<n and j<m):
    if(arr1[i]==arr2[j]):
        a.append(arr1[i])
        i=i+1
        j=j+1
    elif(arr1[i]<arr2[j]):
        a.append(arr1[i])
        i=i+1
    elif(arr2[j]>arr1[i]):
        a.append(arr2[j])
        j=j+1
        
if(n>m):
    for i in range(m+1,n+1):
        a.append(i)
        i=i+1
elif(m>n):
    for j in range(n+1,m+1):
        a.append(j)
        j=j+1
    
print(a)
        