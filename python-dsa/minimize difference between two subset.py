# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:36:13 2021

@author: Abhishek Parashar
"""
import sys
def subsetsum(n,arr):
    w=0
    for i in arr:
        w=w+i
    t= [[False for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        t[i][0]=True
    for i in range(w+1):
        t[0][i]=False
    for i in range(n+1):
        for j in range(w+1):
            if (arr[i-1]<=j):
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            elif(arr[i-1]>j):
                t[i][j]=t[i-1][j]
    diff=sys.maxsize
    for i in range(w//2,-1,-1):
        if(t[n][j==True]):
            diff=w-2*j
            break
        return diff
arr = [ 3, 1, 4, 2, 2, 1 ]
n = len(arr)
print(subsetsum(n,arr))
     
            
        
            
            