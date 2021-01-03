# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:17:21 2021

@author: Abhishek Parashar
"""
def uknap(val,n,cuts):
    t=[[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if(cuts[i-1]<=j):
                t[i][j]=max(val[i-1]+t[i][j-cuts[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][n]
cuts=[1,2,3,4,5,6,7,8]
val=[1,5,8,9,10,17,17,20]
n=8
print(uknap(val,n,cuts))
    
    