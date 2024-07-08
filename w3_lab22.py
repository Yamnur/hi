# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:54:06 2024

@author: cseweb
"""

s=input("enter a string:").split(" ")
for i in s:
      print(i[-1::-1],end=" ")
print()
print("reversed sentence=" ".join(s[-1::-1]))