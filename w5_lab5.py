# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:44:42 2024

@author: cseweb
"""

st=input("enter string").split(" ")
d={}
for i in st:
    x=i.split("-")
    for j in range(2):
        d[x[0]]=x[1]
print(d)
import json
d1="{a:1,b:2}"
res=json.loads(d1)
print(str(res))
