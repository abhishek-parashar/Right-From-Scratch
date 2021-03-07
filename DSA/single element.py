# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:31:29 2020

@author: Abhishek Parashar
"""

#program to find single element 
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans=ans^a[i]
    print(ans)
