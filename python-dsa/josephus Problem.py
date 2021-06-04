# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:03:22 2020

@author: Abhishek Parashar
"""

def solve(arr,k,index,ans):
    if len(arr)==1:
        ans=arr[0]
        return
    index=(index+k)%len(arr)
    arr.pop(index)
    solve(arr,k,index,ans)
    return
t=int(input())
while(t>0):
    s=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    k=s[1]
    k=k-1
    index=0
    ans=-1