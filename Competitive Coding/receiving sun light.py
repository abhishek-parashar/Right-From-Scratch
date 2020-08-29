# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:26:45 2020

@author: Abhishek Parashar
"""
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    s.append(a[0])
    for i in range(1,n):
        if (a[i]>a[i-1]):
            s.append(a[i])
    c=len(s)
    print(c)
    t=t-1
            
        

