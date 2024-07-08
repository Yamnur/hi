# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:01:48 2024

@author: cseweb
"""

s=input("enter a string:")
fd=False
fa=False
for i in s:    
   if(i.isalpha()):
       fa=True
   if(i.isdigit()):
       fd=True
if(fa==True and fd==True):
    print("string containing letter and digit")
else:
    print("-1")
      