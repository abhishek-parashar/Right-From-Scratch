# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:49:36 2020

@author: Abhishek Parashar
"""
a=[1,2,3,-1,-2,-6,-9,9,8,7,0,-5,-11]
i=0
j=len(a)-1
while(i<j):
    if(a[i]<0 and a[j]<0):
        i=i+1
    elif(a[j]>0 and a[i]>0):
        j=j-1
    elif(a[i]>0 and a[j]<0):
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
    else:
        i=i+1
        j=j-1
print(a)
        
