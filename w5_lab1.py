# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:56:41 2024

@author: cseweb
"""
n=int(input("enter n"))
dict={}
for i in range(n+1):
    if(i%2!=0):
        dict[i]=i**3
print(dict)