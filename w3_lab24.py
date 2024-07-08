# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:39:04 2024

@author: cseweb
"""

s=input("enter string ")
for i in s:
    if( i==','):
       print(i.replace(i,'.'),end="")
    elif (i=='.'):
       print(i.replace(i,','),end="")
    else:
        print(i,end="")