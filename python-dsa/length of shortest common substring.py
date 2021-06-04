# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 01:39:32 2021

@author: Abhishek Parashar
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        t=[[0 for i in range(n+1)]for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if(str1[i-1]==str2[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=1+min(t[i-1][j],t[i][j-1])
        index=t[n][m]
        i=n
        j=m
        string=""
        while(i>0 and j>0):
            if(str1[i-1]==str2[j-1]):
                string=string+str1[i-1]
                i=i-1
                j=j-1
                index=index-1
            elif(str1[i-1][j]>str2[i][j-1]):
                string=string+str2[j-1]
                j=j-1
                index=index-1
            else:
                string=string+str[i-1]
                i=i-1
                index=index-1
        while(i>0):
            string=string+str1[i-1]
            i=i-1
            index=index-1
        while(j>0):
            string=string+str2[j-1]
            j=j-1
            index=index-1
        string = list(string) 
        string.reverse() 
        return ''.join(string) 