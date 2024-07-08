# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:41:28 2024

@author: cseweb
"""

n=int(input("enter n"))
if(n<1):
    print("1 is not prime")
else:
    for i in range(2,n//2+1):
        if(n%i==0):
            print("not a prime number")
            break
    else:
        print("prime")