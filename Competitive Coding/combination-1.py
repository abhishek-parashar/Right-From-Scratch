# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:01 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index,k):
    if len(subset)==k:
        print(*subset)
    for i in range(index,len(arr)):
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,k)
        subset.pop(-1)
    return
def subset(arr):
    global res
    subset=[]
    index=0
    k=2
    subsetutil(arr, subset, index,k)
    return
array=[1,2,3]
subset(array)