# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:50:55 2024

@author: cseweb
"""

s=input("enter a string:")
s=s.lower()
s1="aeiou"
for i in s:
    if i in s1:
        pass
    else:
        print(i,end="")