# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:06:08 2021

@author: Abhishek Parashar
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        t=[[sys.maxsize-1 for i in range(amount+1)]for i in range(n+1)]
        for i in range(1,n+1):
            t[i][0]=0
        for i in range(1,amount+1):
            if(i%coins[0]==0):
                t[1][i]=i//coins[0]
            else:
                t[1][i]=sys.maxsize-1
        for i in range(n+1):
            for j in range(amount+1):
                if(coins[i-1]<=j):
                    t[i][j]=min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        if(t[n][amount]==sys.maxsize-1):
            return -1
        else: 
            return t[n][amount]