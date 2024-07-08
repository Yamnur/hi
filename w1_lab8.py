# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:54:26 2024

@author: cseweb
"""
n=int(input("enter n"))
l=[]
print("enter %d number"%n)
for i in range(n):
    k=int(input())
    l.append(k)
ec=0
esum=0
oc=0
osum=0
for i in l:
    if(i%2==0):
        esum+=i
        ec+=1
    else:
        osum+=i
        oc+=1
print('even count=',ec,'even sum',esum)
print('odd count=',oc,'odd sum',osum) 
        