# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:50:43 2020

@author: Abhishek Parashar
"""

t=int(input()) 
#t is no of test cases
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    start=0
    end=n-1
    def minimum_ele(start,end,arr):
        if(arr[start]==arr[end]):
            return arr[start]
        if(end==start+1):
            if(arr[start]>arr[end]):
                return arr[end]
            else:
                return arr[start]
        else:
            mid=(start+end)//2
            if(arr[mid]<=arr[mid+1] and arr[mid]<=arr[mid-1]):
                return arr[mid]
            if(arr[start]<=arr[mid]):
                start=mid+1
                return minimum_ele(start,end,arr)
            elif(arr[mid]<=arr[end]):
                end=mid-1
                return minimum_ele(start,end,arr)
    print(str(minimum_ele(start,end,a)))
    t=t-1

    