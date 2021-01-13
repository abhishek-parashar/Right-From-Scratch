# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:56:33 2021

@author: Abhishek Parashar
"""
arr=[4, 5, 6, 7, 6]
k=1
x=6
n=len(arr)
def search(arr,x,k,n):
    i=0
    while(i<=n):
        if(arr[i]==x):
            return i
        i=i+max(1,int(abs(arr[i]-x)/k))
    return -1
print(search(arr,x,k,n))