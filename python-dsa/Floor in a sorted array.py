# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:27:47 2020

@author: Abhishek Parashar
"""

t=int(input())
while(t>0):
    inpt=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    n=inpt[0]
    x=inpt[1]
    end=len(arr)-1
    start=0
   
    def search(arr,start,end,x):
        mid=(start+end)//2
        if(start>end):
            return -1
        if(arr[mid-1]<x and arr[mid]>x):
            return arr[mid-1]
        if (arr[end]<x):
            return arr[end]
        if(arr[mid]==x):
            return arr[mid]
        elif(arr[mid]<x):
            return search(arr,mid+1,end,x)
        else:
            return search(arr,start,mid-1,x)
        
    s=search(arr,start,end,x)
    print(s)
    t=t-1