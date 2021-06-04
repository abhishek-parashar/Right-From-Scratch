# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:54:34 2021

@author: Abhishek Parashar
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        t=[[-1 for i in range(N+1)]for i in range(K+1)]
        if(N==0 or N==1):
            return N
        if(K==1):
            return N
        if(t[K][N]!=-1):
            return t[K][N]
        mn = sys.maxsize
        for z in range(1,N):
            temp=1+max(Solution.superEggDrop(self,K-1,z-1),Solution.superEggDrop(self,K,N-z))
            mn=min(mn,temp)
        t[K][N]=mn
        return t[K][N]