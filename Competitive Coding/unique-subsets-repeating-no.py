# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:01 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index):
    print(*subset)
    for i in range(index,len(arr)):
        if (i>index and arr[i]==arr[i-1]):
            continue
        subset.append(arr[i])
        subsetutil(arr,subset,i+1)
        subset.pop(-1)
    return
def subset(arr):
    global res
    subset=[]
    index=0
    subsetutil(arr, subset, index)
    return
array=[1,2,2]
subset(array)