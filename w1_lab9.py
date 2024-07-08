# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:47:46 2024

@author: cseweb
"""
m=int(input("enter m"))
n=int(input("enter n"))
for j in range(m,n+1):
   if(j>1):
     for i in range(2,j//2+1):
        if(j%i==0):
            break
     else:
        print(j)
