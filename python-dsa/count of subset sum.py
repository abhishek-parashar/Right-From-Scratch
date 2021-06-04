# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:00:15 2021

@author: Abhishek Parashar
"""

def subsetsum(arr,n,w):
    t=[[0 for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        t[i][0]=1
    for i in range(w+1):
        t[0][i]=0
    for i in range(n+1):
        for j in range(w+1):
            if(arr[i-1]<j):
                t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
            if(arr[i-1]>j):
                t[i][j]=t[i-1][j]
    return t[n][w]
arr=[1,2,3,3]
w=6
n=len(arr)
print(subsetsum(arr,n,w))