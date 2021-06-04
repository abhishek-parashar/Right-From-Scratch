# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:47:07 2021

@author: Abhishek Parashar
"""

def uknap(w,arr,n):
    t=[[0 for i in range(w)]for i in range(n+1)]
    for i in range(n+1):
        t[i][0]=1
    for i in range(n+1):
        for j in range(w):
            if(arr[i-1]<=j):
                t[i][j]=t[i][j-arr[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][w-1]
arr=[1,2,3]
w=4
n=len(arr)
print(uknap(w,arr,n))