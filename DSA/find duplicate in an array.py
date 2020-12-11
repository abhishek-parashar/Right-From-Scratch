# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
arr=[1, 2, 3, 4, 5, 6, 3 ]
n=len(arr)
slow=arr[0]
fast=arr[arr[0]]
while(slow!=fast):
    slow=arr[slow]
    fast=arr[arr[fast]]
fast=0
while(slow!=fast):
    slow=arr[slow]
    fast=arr[fast]
print(slow)