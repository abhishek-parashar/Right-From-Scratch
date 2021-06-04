# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:17:58 2020

@author: Abhishek Parashar
"""
def findCandidate(A):
    cand=[]
    num1=-1
    num2=-1
    c1=0
    c2=0
    for i in A:
        if i==num1:
            c1=c1+1
        elif i==num2:
            c1=c2+1
        elif c1==0:
            num1=i
            c1=1
        elif c2==0:
            num2=i
            c2=1
        else:
            c1=c1-1
            c2=c2-1
    count1=0
    count2=0
    for i in A:
        if i==num1:
            count1=count1+1
        elif i==num2:
            count2=count2+1
    if count1>len(A)/3:
        cand.append(num1)
    if count2>len(A)/3:
        cand.append(num2)
    return cand
A=[1, 2, 3, 1, 1 ]
f=findCandidate(A)
print(f) 
    


