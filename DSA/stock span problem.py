# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:49:27 2020

@author: Abhishek Parashar
"""




stack=[[]]
vector=[]
arr=[1,3,2,4]
for i in range(len(arr)):
    if (len(stack)==0):
        vector.append(-1)
    elif (len(stack)>0 and stack[-1][0]>=arr[i]):
        vector.append(stack[-1][1])
    elif (len(stack)>0 and stack[-1][0]<=arr[i]):
        while(len(stack)>0 and stack[-1][0]<=arr[i]):
            stack.pop(-1)
        if(len(stack)==0):
            vector.append(-1)
        else:
            vector.append(stack[-1][1])
    stack.append([arr[i],i])
print(vector)
            