# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:35:56 2024

@author: cseweb
"""
from math import *
ang=30
x=radians(ang)
n=int(input("enter no of terms"))
sin_app=0
for i in range (n):
    term=((-1)**i *x**(2*i+1))/factorial(2*i+1)
    sin_app+=term
print(sin_app)