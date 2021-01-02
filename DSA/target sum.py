# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:37:04 2021

@author: Abhishek Parashar
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum=0
        for i in nums:
            sum = sum + i
        w=(sum+S)//2
        n=len(nums)
        t=[[0 for i in range(w+1)] for i in range(n+1)]
        for i in range(n+1):
            t[i][0]=1
        for i in range(w+1):
            t[0][i]=0
        for i in range(n+1):
            for j in range(w+1):
                if(nums[i-1]<=j):
                    t[i][j]=t[i-1][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][w]
        