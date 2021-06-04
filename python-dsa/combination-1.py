# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:01 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index,k,ans):
    if len(subset)==k:
        ans.append(subset[:])
        return
    for i in range(index,len(arr)):
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,k,ans)
        subset.pop(-1)
    return ans

subset=[]
index=0
k=2
arr=[1,2,3]
ans=[]
subsetutil(arr, subset, index,k,ans)
print(*ans)
