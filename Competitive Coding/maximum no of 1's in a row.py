# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:56:14 2020

@author: Abhishek Parashar
"""
arr=list(map(int,input().strip().split()))
m=arr[0] #row
n=arr[1] #column
a=list(map(int,input().strip().split()))
mat=[[0 for i in range(n)] for j in range(m)]
c=0
for i in range(m):
    for j in range(n):
        mat[i][j]=a[c]
        c=c+1
max=0
#print(mat)
index=-1
for i in range(m):
    conut=0
    count=mat[i].count(1)
    if count>max:
        max=count
        index=i
print(index)