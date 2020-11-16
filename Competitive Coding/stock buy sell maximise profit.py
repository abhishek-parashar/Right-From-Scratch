# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:14:11 2020

@author: Abhishek Parashar
"""
price = [100, 180, 260, 310, 40, 535, 695]
n=len(price)
i=0
while(i<n-1):
    while(i<n-1 and price[i+1]<=price[i]):
       i=i+1
    if(i==n-1):
        break
    buy=i
    i=i+1
    while(i<n and price[i]>=price[i-1]):
        i=i+1
    sell=i-1
    print("buy on day",buy,"\t")
    print("sell on day",sell)
        
    