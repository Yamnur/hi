# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:31:26 2024

@author: cseweb
"""
from math import *
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b*b-4*a*c
if(d==0):
    root=-b/(2*a)
    print("roots are real and equal ")
    print("root=",root)
elif(d>0):
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print("roots are real and differ ")
    print("root1=",r1) 
    print("root2=",r2)
else:
     print("roots are imaginary ")
    