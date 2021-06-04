# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:01 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index,ans):
    ans.append(subset[:])
    for i in range(index,len(arr)):
        if (i>index and arr[i]==arr[i-1]):
            continue
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,ans)
        subset.pop(-1)
    return ans

ans=[] 
subset=[]
index=0
arr=[1,2,2]
subsetutil(arr, subset, index,ans)
print(*ans)
