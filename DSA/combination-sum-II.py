# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:11:31 2020

@author: Abhishek Parashar
"""


def subsetutil(arr, subset, index,target,ans):
    if(target<0):
        return
    elif(target==0):
        ans.append(subset[:])
    for i in range(index,len(arr)):
        if (i>index and arr[i]==arr[i-1]):
            continue
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,target-arr[i],ans)
        subset.pop(-1)
    return ans

ans=[] 
subset=[]
index=0
arr=[1,2,2,2,2,3,3,4,7]
target=8
subsetutil(arr, subset, index,target,ans)
print(*ans)
