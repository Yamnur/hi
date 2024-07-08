# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:28:22 2024

@author: cseweb
"""

from datetime import datetime
now=datetime.now()
y=now.year
d=now.day
m=now.strftime("%B")
#print("current time=",now)
print(d,m,y,sep="-")
if(y%400==0 or y%4==0 and y%100!=0):
    print("leaf year")
else:
    print("not ")
    