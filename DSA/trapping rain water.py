# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:49:56 2020

@author: Abhishek Parashar
"""
arr=[3,0,0,2,4]
n=len(arr)
mxl=[n]
mxr=[n]
arr=[3,0,0,2,4]
n=len(arr)
mxl=mxl.append(arr[0])
for i in range(len(arr)):
    mxl[i]=max(mxl[i-1],arr[i])
mxr=arr[n]
for i in range(n-2,0,-1):
    mxr[i]=max(mxr[i+1],arr[i])
water=[]
for i in range(n):
    water[i]=min(mxr[i],mxl[i])-arr[i]
    sum=sum+water[i]
print(*sum)