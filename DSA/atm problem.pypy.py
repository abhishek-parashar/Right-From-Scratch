# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:43:22 2021

@author: Abhishek Parashar
"""

a=list(map(float,input().split()))
if (a[0]%5==0):
    a[0]=a[0]+0.5
    a[1]=a[1]-a[0]
    print(a[1])
else:
    print(a[1])