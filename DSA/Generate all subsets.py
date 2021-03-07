# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:01 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index,ans):
    ans.append(subset[:])
    for i in range(index,len(arr)):
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,ans)
        subset.pop(-1)
    return ans

subset=[]
index=0
ans=[]
arr=[1,2,3]
subsetutil(arr, subset, index,ans)
print(*ans)