# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:11:42 2024

@author: cseweb
"""

import re
s=input("enter passport number")
a=r'[A-Z][1-9][0-9]\s{0,1}[0-9]{4}[1-9]|[A-Z][1-9][0-9][0-9]{4}[1-9]'
x=re.search(a,s)
if x:
     print("valid")
else:
    print("not")