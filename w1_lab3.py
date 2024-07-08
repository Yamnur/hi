# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:16:33 2024

@author: cseweb
"""

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a>b):
    if(a>c):
        print(a)
    else:
        if(c>b):
            print(c)
        else:
            print(b)
else:
    if(b>c):
        print(b)
    else:
        print(c)
       
