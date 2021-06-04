# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:54:42 2021

@author: Abhishek Parashar
"""

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n=len(s1)
        if(len(s1) != len(s2)):
            return False
        if not n:
            return True
        if s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        for i in range(1,n):
            if(Solution.isScramble(self,s1[:i], s2[:i]) and
            Solution.isScramble(self,s1[i:], s2[i:])):
                return True
            if (Solution.isScramble(self,s1[-i:], s2[:i]) and
            Solution.isScramble(self,s1[:-i], s2[i:])):
                return True
        return False