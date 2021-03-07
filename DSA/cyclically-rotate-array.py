# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:40:20 2020

@author: Abhishek Parashar
"""

t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,a[-1])
    a.pop()
    print(a)