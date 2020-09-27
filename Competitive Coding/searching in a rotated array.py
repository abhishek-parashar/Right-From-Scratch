# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:24:34 2020

@author: Abhishek Parashar
"""

## searching an element in rotated sorted array
def search(arr,start,end,key):
    # if overflow
    if start>end:
        return -1
    # if the midlle element is the element
    mid=(start+end)//2
    if arr[mid]==key:
        return mid
    # if array start....mid is not rotated
    if(arr[start]<arr[mid]):
        if(key>=arr[start]and key<arr[mid]):
            return search(arr,start,mid-1,key)
        return search(arr,mid+1,end,key)
    # if array mid ... end is not rotated
    if(arr[mid]<=arr[end]):
        if(key>=arr[mid]and arr[end]>=key):
            return search(arr,mid+1,end,key)
        return search(arr,start,mid-1,key)
    else:
        return -1
t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    start=0
    end=n-1
    i=search(a,start,end,k)
    print(i)
    t=t-1