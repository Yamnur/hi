# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:36:51 2024

@author: cseweb
"""

n=int(input("enter n"))
f=1
for i in range(1,n+1):
    f=f*i
    print('fact of %d =%d'%(i,f))

