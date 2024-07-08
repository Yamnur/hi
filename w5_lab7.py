# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:49:29 2024

@author: cseweb
"""

def sum_na(n):
    if n==0 or n==1:
        return n
    else:
        return n+sum_na(n-1)
n=int(input("enter n"))
print("sum of n natural nos=",sum_na(n))

    