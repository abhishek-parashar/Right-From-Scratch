# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:52:12 2020

@author: Abhishek Parashar
"""
def solve(ip,op):
    if len(ip)==0:
        print(op)
        return
    op1=op
    op2=op
    op1.append(" ")
    op1.append(ip[0])
    op2.append(ip[0])
    ip.pop(0)
    solve(ip,op1)
    solve(ip,op2)
    return
t=int(input())
while(t>0):
    n=int(input())
    ip=list(str(input()))
    op=[]
    op.append(ip[0])
    ip.pop(0)
    solve(ip,op)
    t=t-1