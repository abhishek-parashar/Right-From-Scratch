# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:54:06 2020

@author: Abhishek Parashar
"""
t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    n=int(input())
if(n==2):
    d=a[0]+a[1]//2
else:
    d1=a[1]-a[0]
    d2=a[2]-a[1]
    if(d1==d2):
        d=d1
    else:
        d=d2
    for i in range(n+1):
        if(a[i]!=a[0]+(i*d)):
            s=a[0]+(i*d)
            print(s)
            
