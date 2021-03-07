# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:20:18 2020

@author: Abhishek Parashar
"""

def subsetutil(arr, subset, index,target,ans,k):
    if(len(subset)==k):
        if(target<0):
            return
        elif(target==0):
            ans.append(subset[:])
            return
    for i in range(index,len(arr)):
        if (i>index and arr[i]==arr[i-1]):
            continue
        subset.append(arr[i])
        subsetutil(arr,subset,i+1,target-arr[i],ans,k)
        subset.pop(-1)
    return ans

ans=[] 
subset=[]
index=1
k=2
arr=[1,2,3,4,5,6,7,8,9]
target=8
subsetutil(arr, subset, index,target,ans,k)
print(*ans)
