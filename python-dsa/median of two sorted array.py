# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:40:28 2020

@author: Abhishek Parashar
"""

nums1=[1,2,5]
nums2=[3,4]
i=0
j=0
arr3=[]
n1=len(nums1)
n2=len(nums2)
while(i<n1 and j<n2):
    if(nums1[i]<nums2[j]):
        arr3.append(nums1[i])
        i=i+1
    else:
        arr3.append(nums2[j])
        j=j+1
if(n1>n2):
    for i in range(n2,n1):
        arr3.append(nums1[i])
elif(n2>n1):
    for i in range(n1,n2):
        arr3.append(nums2[i])
start=arr3[0]
end=arr3[len(arr3)-1]
median=(start+end)/2
print(median)