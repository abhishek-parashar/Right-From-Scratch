# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:23:55 2021

@author: Abhishek Parashar
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetsum(nums,n,w):
            t=[[False for i in range(w+1)]for i in range(n+1)]
            for i in range(n+1):
                t[i][0]=True
            for i in range(1,w+1):
                t[0][i]=False
            for i in range(n+1):
                for j in range(w+1):
                    if(nums[i-1]<=w):
                        t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                    elif(nums[i-1]>w):
                        t[i][j]=t[i-1][j]
            return t[n][w]
        n=len(nums)
        sum=0
        for i in nums:
            sum=sum+i
        if(sum%2==0):
            w=sum//2
            return subsetsum(nums,n,w)
        else:
            return False
    