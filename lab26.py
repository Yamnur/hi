# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:03:39 2024

@author: cseweb
"""
s=input("enter 4 digit binsry number:").split(',')
for i in s:
    d=int(i,2)
    if(d%5==0):
        print(i,"divisible by 5")
    else:
        print(i,"not divisible by 5")
        


