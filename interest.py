# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:04:10 2024

@author: cseweb
"""

p=int(input("enter principle amt"))
r=int(input("entrer rate of interest"))
t=int(input("entre time in year"))
R=1+(r/100)
si=(p*t*r)/100
print("simple=",si)

ci=p*pow(R,t)-p
print("comp=",ci)
if(si>=ci):
    print("si is greater then ci")
else:
    print("ci is greater then si")
