# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:38:47 2020

@author: Abhishek Parashar
"""
arr=[-2, -3, 4, -1, -2, 1, 5, -3] 
csum=arr[0]
osum=arr[0]
i=1
for i in range(len(arr)):
    if(csum>=0):
        csum=csum+arr[i]
    else:
        csum=arr[i]
    if(csum>osum):
        osum=csum
print(osum)