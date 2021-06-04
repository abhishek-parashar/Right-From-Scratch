# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:03:23 2020

@author: Abhishek Parashar
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low =0
        high=len(arr)-1
        size=len(arr)
        while(low<=high):
            mid= (high+low)//2
            if(mid>0 and mid<len(arr)-1):
                if (arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                    return mid
                elif(arr[mid-1]>arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
            elif(mid==0):
                if(arr[0]>arr[1]):
                    return 0
                else:
                    return 1
            elif(mid==size-1):
                if(arr[size-1]>arr[size-2]):
                    return size-1
                else:
                    return size-2