# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:16:42 2020

@author: Abhishek Parashar
"""
stack=[]
vector=[]
arr=[4,5,2,10,8]
for i in range(len(arr)-1,0,-1):
    if (len(stack)==0):
        vector.append(-1)
    elif (len(stack)>0 and stack[-1]<arr[i]):
        vector.append(stack[-1])
    elif (len(stack)>0 and stack[-1]>=arr[i]):
        while(len(stack)>0 and stack[-1]>=arr[i]):
            stack.pop(-1)
        if(len(stack)==0):
            vector.append(-1)
        else:
            vector.append(stack[-1])
    stack.append(arr[i])
print(vector[: :-1])
            
        
        