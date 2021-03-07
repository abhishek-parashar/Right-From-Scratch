# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:11:23 2020

@author: Abhishek Parashar
"""

def subsetsum(arr,w,n):
    t=[[False for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        t[i][0]=True
    for i in range(1,w+1):
        t[0][i]=False
    for i in range(1,n+1):
        for j in range(1,w+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            elif(arr[i-1]>j):
                t[i][j]=t[i-1][j]
    return t[n][w]
arr = [3, 34, 4, 12, 5, 2]
w=9
n=len(arr)
print(subsetsum(arr,w,n))
