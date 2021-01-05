# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:54:11 2021

@author: Abhishek Parashar
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        t=[[0 for i in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(word1[i-1]==word2[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        x=t[n][m]
        y=n-x
        z=m-x
        return y+z
        