# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:11:17 2020

@author: Abhishek Parashar
"""

t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if(a.count(i)==1):
            print(i)
            break
    t=t-1
    