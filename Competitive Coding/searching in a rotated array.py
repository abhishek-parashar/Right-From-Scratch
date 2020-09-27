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
    # if array is rotated
    if(arr[mid]>=arr[start]):
        if(key>=arr[mid] and key<=arr[end]):
            return search(arr,mid+1,end,key)
        return search(arr,start,mid-1,key)
    # if array is not rotated
    if key >= arr[start] and key <= arr[mid]: 
        return search(arr, start, mid-1, key) 
    return search(arr, mid + 1, end, key)
t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    start=0
    end=n
    i=search(a,start,end,k)
    print(i)
    t=t-1