# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:08:19 2020

@author: Abhishek Parashar
"""

def minimum(i,j):
    start=0
    end=j
    while(start<=end):
        mid=(start+end)//2
        if((a[mid]<=a[mid+1]) and (a[mid]<=a[mid-1])):
            return a[mid]
        elif(a[start]<=a[mid]):
            start=mid+1
        elif(a[mid]<=a[end]):
            end=mid-1
if__name__="__main__"
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split())
    minimum(a,n)
    t=t-1
        