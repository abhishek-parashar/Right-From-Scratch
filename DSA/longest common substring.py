# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:54:12 2021

@author: Abhishek Parashar
"""

#User function Template for python3
def lcs(m,n,X,Y):
    '''
    :param m: length of string X 
    :param n: length of string Y
    :param X: string X
    :param Y: string Y
    :return: Integer
    '''
    # code here
    t=[[0 for i in range(n+1)]for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(X[i-1]==Y[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=0
    return t[m][n]


