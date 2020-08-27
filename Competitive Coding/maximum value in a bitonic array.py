# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Abhishek Parashar
# maximum value in a bitonic array.

 
t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a=list(a)
    print(a[-1])
    t=t-1

