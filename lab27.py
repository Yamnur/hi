# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:19:16 2024

@author: cseweb
"""

l="abcdefghijklmnopqrstuvwxyz"
s=input("enter string ")
s=s.lower()
p=False
for i in l:
    if(i not in s):
        p=False
    else:
        p=True
if(p==True):
    print("pangram")
else:
    print("not")
    
    