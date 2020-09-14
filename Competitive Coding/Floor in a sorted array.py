# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:32:44 2020

@author: Abhishek Parashar
"""
t=int(input())
while(t>0):
    inpt=list(map(int,input().split()))
    a=list(map(int,input().split()))
    n=inpt[0]
    x=inpt[1]
    s=[]
    for i in range(n+1):
        if(a[0]>x):
            print(-1)
            break
        elif(a[i]<x):
            s.append(a[i])
        print(s[-1])
    t=t-1
    