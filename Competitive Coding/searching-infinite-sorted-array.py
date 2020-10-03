# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:56:22 2020

@author: Abhishek Parashar
"""
start=0
end=1
x=int(input())
arr=int(input())
while(end<x):
    start=end
    end=end*2
while(end>start):
    mid=(start+end)//2
    if(arr[mid]==x):
        print(mid)
    elif(arr[mid]>x):
        end=mid-1
    elif(arr[mid]<x):
        start=mid+1
    else:
        print(-1)
    
